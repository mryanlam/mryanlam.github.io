---
title: "OCI OS for Blog Gallery"
date: 2026-04-04
description: "How to use Oracle Cloud Infrastructure (OCI) Object Storage to power high-performance, cost-effective image galleries in Hugo."
summary: "Learn how to offload your blog's media to OCI Object Storage while maintaining a seamless gallery experience using custom Hugo shortcodes and the Blowfish theme."
tags: ["Technical", "OCI", "Cloud", "Hugo", "Shortcodes"]
---

Modern static sites are fast, but hosting hundreds of high-resolution images can quickly bloat your repository and slow down your build times. In this post, I'll walk through how I use **Oracle Cloud Infrastructure (OCI) Object Storage** to host my travel photos and pull them dynamically into my Hugo blog using a custom shortcode.

## Why OCI Object Storage?

OCI Object Storage is an enterprise-grade storage solution that is incredibly cost-effective—Oracle's **Always Free** tier currently provides up to **20 GB** of storage, which is more than enough for most personal blogs. By offloading images to the cloud:
- **Repo stays light**: Your Git repository only contains code and configuration.
- **Global Delivery**: Images are served via Oracle's high-speed backbone.
- **Organization**: You can manage thousands of files using prefixes and buckets.

## 1. Organizing Your Assets

While Object Storage is "flat," you can simulate a folder structure using **prefixes**. For my trips, I organize images like this:

- `2024_japan/day_1/image1.jpg`
- `2024_japan/day_1/image2.jpg`
- `2024_japan/day_2/image3.jpg`

When uploading via the OCI Console or CLI, simply include the prefix in the object name to "create" these folders.

## 2. Pre-Authenticated Requests (PARs)

To keep your bucket private while still allowing your blog to display images, we use **Pre-Authenticated Requests (PARs)**. 

A PAR is a unique URL that grants read access to a specific object (or an entire bucket) without requiring the user to authenticate. This allows you to:
- Avoid making your entire bucket public.
- Provide a direct link that Hugo can embed in an `<img>` tag.
- Set expiration dates for links.

## 3. Creating the Manifest

Since we don't want to manually type hundreds of URLs, we use a JSON manifest file (`oci_manifest.json`) located in the post's bundle. This file acts as a database for our shortcode.

```json
{
    "day_1": [
        {
            "file_name": "PXL_20241125_160934189.jpg",
            "object_path": "2024_japan/day_1/PXL_20241125_160934189.jpg",
            "par_url": "https://objectstorage.us-phoenix-1.oraclecloud.com/p/..."
        }
    ]
}
```

## 4. Automated Workflow with OCI Python SDK

While you can manage this process manually via the OCI Console, it's far more efficient to automate it. Here are the key excerpts from my sync script using the **OCI Python SDK**.

### 📁 Expected Local Structure
Before running the script, I organize my photos locally to match how I want them grouped in the blog's manifest. The script is designed to traverse a main directory and treat each sub-folder as a separate category (e.g., by day).

**Local structure example:**
*   `2026_japan/` (The root directory)
    *   `day_1/`
        *   `sunset.jpg`
        *   `sushi_dinner.jpg`
    *   `day_2/`
        *   `mt_fuji_hike.jpg`

By "walking" this local directory, the script automatically uses the folder names as keys in our JSON manifest. This allows our Hugo shortcode to easily pull images for a specific day just by referencing the folder name.

### 🔧 Setting Up the Client
First, we initialize the Object Storage client using the standard OCI configuration file (normally located at `~/.oci/config`).

```python
import oci

def get_storage_client():
    # Load config and initialize client
    config = oci.config.from_file()
    client = oci.object_storage.ObjectStorageClient(config)
    namespace = client.get_namespace().data
    return client, namespace
```

### 🔐 Programmatic PAR Generation
The core of the security model is generating a **Pre-Authenticated Request** for each object. This allows the blog to access the images securely without making the bucket public.

```python
from datetime import datetime, timedelta, timezone

def create_par(client, namespace, bucket, object_name):
    # Set expiration (e.g., 5 years)
    expiry_time = datetime.now(timezone.utc) + timedelta(days=PAR_EXPIRY_DAYS)
    
    par_details = oci.object_storage.models.CreatePreauthenticatedRequestDetails(
        name=f"PAR_{object_name.replace('/', '_')}",
        access_type="ObjectRead",
        object_name=object_name,
        time_expires=expiry_time
    )
    
    par_response = client.create_preauthenticated_request(namespace, bucket, par_details)
    return f"https://objectstorage.us-phoenix-1.oraclecloud.com{par_response.data.access_uri}"
```

### 🚀 Syncing the Gallery
Finally, we walk through the local directory, upload any missing images, and populate our JSON manifest.

```python
for root, dirs, files in os.walk(LOCAL_DIRECTORY):
    for file in files:
        # Check if object already exists in OCI
        if not object_exists(client, namespace, BUCKET_NAME, object_name):
            print(f"Uploading: {object_name}")
            with open(local_path, "rb") as f:
                client.put_object(namespace, BUCKET_NAME, object_name, f)
                par_url = create_par(client, namespace, BUCKET_NAME, object_name)
                # Store metadata in manifest results...
```

This automation ensures that your blog galleries are always in sync with your cloud storage with just a single command.

## 5. The Hugo Shortcode: `oci_gallery`

I created a custom shortcode called [oci_gallery.html](https://github.com/mryanlam/mryanlam.github.io/blob/master/layouts/shortcodes/oci_gallery.html) that reads this JSON file and generates standard HTML `<img>` tags.

```html
{{ $day := .Get "day" }}
{{ $class := .Get "class" | default "grid-w50 md:grid-w33 xl:grid-w25" }}
{{ $jsonFile := .Page.Resources.GetMatch "oci_manifest.json" }}

{{ if $jsonFile }}
  {{ $data := $jsonFile.Content | transform.Unmarshal }}
  {{ $images := index $data $day }}
  {{ range $images }}
    <img src="{{ .par_url }}" class="{{ $class }}" />
  {{ end }}
{{ end }}
```

## 6. Integrating with Blowfish

The beauty of this setup is that it plays perfectly with the **Blowfish** theme's built-in gallery shortcode. By wrapping our custom shortcode inside the theme's gallery, we get all the responsive grid styling and lightbox functionality for free:

```markdown
{{</* gallery */>}}
  {{</* oci_gallery day="day_1" */>}}
{{</* /gallery */>}}
```

## Conclusion

By combining OCI Object Storage with Hugo's powerful data-processing capabilities, you can build media-rich blogs that are both performant and easy to maintain. No more `git push` struggles with 50MB of images!

Check out my [Japan 2024]({{< ref "japan-2024" >}}) post to see this in action!
