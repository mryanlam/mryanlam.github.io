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

While you can manage this process manually via the OCI Console, it's far more efficient to automate it. Using the **OCI Python SDK**, you can write a simple script to:
1. **Upload**: Scan a local directory of images and upload them with the correct prefixes.
2. **Generate PARs**: Programmatically create a Pre-Authenticated Request for each image.
3. **Generate Manifest**: Write the resulting URLs and metadata into the `oci_manifest.json` file for immediate use in Hugo.

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
