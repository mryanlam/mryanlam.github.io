import oci
import os
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
import typer

app = typer.Typer(add_completion=False)

def get_storage_client(config_path: Path, verbose: bool = False):
    resolved_path = os.path.abspath(os.path.expanduser(str(config_path)))
    if verbose:
        print(f"Loading OCI config from: {resolved_path}")
    
    if not os.path.exists(resolved_path):
        raise FileNotFoundError(f"OCI config file not found at {resolved_path}")

    config = oci.config.from_file(file_location=resolved_path)
    client = oci.object_storage.ObjectStorageClient(config)
    namespace = client.get_namespace().data
    
    if verbose:
        print(f"Successfully connected. Namespace: {namespace}")
    return client, namespace, config

def object_exists(client, namespace, bucket, object_name):
    try:
        client.head_object(namespace, bucket, object_name)
        return True
    except oci.exceptions.ServiceError as e:
        if e.status == 404:
            return False
        raise

def create_par(client, namespace, bucket, object_name, expiry_days: int, region: str):
    expiry_time = datetime.now() + timedelta(days=expiry_days)
    
    par_details = oci.object_storage.models.CreatePreauthenticatedRequestDetails(
        name=f"PAR_{object_name.replace('/', '_')}",
        access_type="ObjectRead",
        object_name=object_name,
        time_expires=expiry_time
    )
    
    par_response = client.create_preauthenticated_request(namespace, bucket, par_details)
    base_url = f"https://objectstorage.{region}.oraclecloud.com"
    return f"{base_url}{par_response.data.access_uri}"

def load_manifest(filepath: Path):
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {}

@app.command()
def sync(
    local_dir: Path = typer.Argument(
        ...,
        help="Local directory containing files to sync.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
    prefix: Optional[str] = typer.Option(
        None,
        "--prefix", "-p",
        help="Prefix folder in the OCI bucket. Defaults to the base name of the local directory.",
    ),
    bucket: str = typer.Option(
        "mbucket",
        "--bucket", "-b",
        help="OCI bucket name.",
    ),
    manifest: Path = typer.Option(
        Path("oci_manifest.json"),
        "--manifest", "-m",
        help="Path to load and save the JSON manifest file.",
    ),
    oci_config: Path = typer.Option(
        Path("~/.oci/config"),
        "--oci-config",
        help="Path to the OCI configuration file.",
    ),
    expiry_days: int = typer.Option(
        1825,
        "--expiry-days",
        help="Number of days for the PAR to expire (default 5 years).",
    ),
    region: Optional[str] = typer.Option(
        None,
        "--region",
        help="Override OCI region for the PAR URL. Defaults to the region set in the OCI config.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Simulate the sync process without making uploads or changing local manifest.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        help="Print verbose debug output.",
    ),
):
    """
    Sync a local directory to Oracle Cloud Infrastructure (OCI) Object Storage
    and generate a JSON manifest with Pre-Authenticated Request (PAR) URLs.
    """
    # 1. Resolve local path and default prefix
    local_dir_path = local_dir.resolve()
    prefix_val = prefix if prefix is not None else local_dir_path.name
    
    if verbose:
        print(f"Local Directory: {local_dir_path}")
        print(f"Target OCI Prefix: {prefix_val}")
        print(f"Target Bucket: {bucket}")
        print(f"Manifest Path: {manifest.resolve()}")
        print(f"PAR Expiry (Days): {expiry_days}")

    # 2. Get storage client and configuration
    try:
        client, namespace, config = get_storage_client(oci_config, verbose=verbose)
    except Exception as e:
        typer.echo(f"Error initializing OCI storage client: {e}", err=True)
        raise typer.Exit(code=1)

    # 3. Determine active region
    active_region = region if region else config.get("region")
    if not active_region:
        active_region = "us-phoenix-1"
        if verbose:
            print(f"No region found in OCI config or options. Defaulting to: {active_region}")
    elif verbose:
        print(f"Using region: {active_region}")

    # 4. Load the manifest
    results = load_manifest(manifest)

    # Walk directory tree
    upload_count = 0
    skip_count = 0

    for root, dirs, files in os.walk(local_dir_path):
        relative_root = os.path.relpath(root, local_dir_path)
        if relative_root == ".":
            relative_root = ""

        for file in files:
            local_path = os.path.join(root, file)
            # Define the object name (the path in the bucket)
            object_name = os.path.join(prefix_val, relative_root, file).replace("\\", "/")
            
            try:
                exists = object_exists(client, namespace, bucket, object_name)
            except Exception as e:
                typer.echo(f"Error checking status for {object_name}: {e}", err=True)
                # In dry_run, we can assume it doesn't exist to show what would be uploaded, 
                # but in real run we should probably stop or fail.
                if dry_run:
                    exists = False
                else:
                    raise typer.Exit(code=1)

            if not exists:
                if dry_run:
                    print(f"[DRY-RUN] Would upload: {object_name} from {local_path}")
                    # Simulate PAR URL
                    par_url = f"https://objectstorage.{active_region}.oraclecloud.com/dummy-access-uri/{object_name}"
                else:
                    print(f"Uploading: {object_name}")
                    with open(local_path, "rb") as f:
                        client.put_object(namespace, bucket, object_name, f)
                    par_url = create_par(client, namespace, bucket, object_name, expiry_days, active_region)
                
                # Store in manifest dictionary
                if relative_root not in results:
                    results[relative_root] = []
                results[relative_root].append({
                    "file_name": file,
                    "object_path": object_name,
                    "par_url": par_url
                })
                upload_count += 1
            else:
                if verbose or not dry_run:
                    print(f"Skipping Image Upload(exists): {object_name}")
                skip_count += 1

    # Save to JSON
    if dry_run:
        print(f"[DRY-RUN] Sync completed (simulated). Would upload {upload_count} files, skip {skip_count} files.")
        print(f"[DRY-RUN] Manifest update (simulated) would be saved to {manifest.resolve()}")
    else:
        # Create manifest parent directory if it doesn't exist
        manifest.parent.mkdir(parents=True, exist_ok=True)
        with open(manifest, "w") as jf:
            json.dump(results, jf, indent=4)
        print(f"\nProcess complete. Folder structure saved to {manifest.resolve()}")
        print(f"Uploaded {upload_count} new files, skipped {skip_count} existing files.")

if __name__ == "__main__":
    app()