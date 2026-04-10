import oci
import os
import json
from datetime import datetime, timedelta, timezone

# --- Configuration ---
BUCKET_NAME = "mbucket"
LOCAL_DIRECTORY = "2026_japan"  # The folder you want to upload
OUTPUT_JSON = "oci_manifest.json"
PAR_EXPIRY_DAYS = 365 * 5  # 5 years

def get_storage_client():
    config = oci.config.from_file()
    client = oci.object_storage.ObjectStorageClient(config)
    namespace = client.get_namespace().data
    return client, namespace

def object_exists(client, namespace, bucket, object_name):
    try:
        client.head_object(namespace, bucket, object_name)
        return True
    except oci.exceptions.ServiceError as e:
        if e.status == 404:
            return False
        raise

def create_par(client, namespace, bucket, object_name):
    # Set expiration date
    expiry_time = datetime.now() + timedelta(days=PAR_EXPIRY_DAYS)
    
    par_details = oci.object_storage.models.CreatePreauthenticatedRequestDetails(
        name=f"PAR_{object_name.replace('/', '_')}",
        access_type="ObjectRead",
        object_name=object_name,
        time_expires=expiry_time
    )
    
    par_response = client.create_preauthenticated_request(namespace, bucket, par_details)
    # The full URL is: https://objectstorage.<region>.oraclecloud.com + access_uri
    region = "us-phoenix-1"  # Update this to your region
    base_url = f"https://objectstorage.{region}.oraclecloud.com"
    return f"{base_url}{par_response.data.access_uri}"

def load_manifest(filepath):
    if os.path.exists(filepath):
        # Standard 'as' keyword is required here
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}


def main():
    client, namespace = get_storage_client()
    results = load_manifest(OUTPUT_JSON)

    for root, dirs, files in os.walk(LOCAL_DIRECTORY):
        # Create a relative path structure for OCI (e.g., folder/subfolder/img.jpg)
        relative_root = os.path.relpath(root, LOCAL_DIRECTORY)
        if relative_root == ".":
            relative_root = ""

        for file in files:
            local_path = os.path.join(root, file)
            # Define the object name (the path in the bucket)
            object_name = os.path.join(LOCAL_DIRECTORY, relative_root, file).replace("\\", "/")
            
            # 1. Check if it exists
            if not object_exists(client, namespace, BUCKET_NAME, object_name):
                print(f"Uploading: {object_name}")
                with open(local_path, "rb") as f:
                    client.put_object(namespace, BUCKET_NAME, object_name, f)
                    par_url = create_par(client, namespace, BUCKET_NAME, object_name)
                    # 3. Store in dictionary for JSON
                    if relative_root not in results:
                        results[relative_root] = []
                    results[relative_root].append({
                        "file_name": file,
                        "object_path": object_name,
                        "par_url": par_url
                    })
            else:
                print(f"Skipping Image Upload(exists): {object_name}")

            

    # 4. Save to JSON
    with open(OUTPUT_JSON, "w") as jf:
        json.dump(results, jf, indent=4)
    
    print(f"\nProcess complete. Folder structure saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()