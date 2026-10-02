# BlizzCon 2026 Post Design Specification

## Overview
This specification defines the structure, metadata, and initial content scaffolding for the blog post covering the trip to California for BlizzCon 2026. Following the decision to separate the overall journey into two distinct posts, this post focuses exclusively on the Anaheim/BlizzCon convention leg, paving the way for a second post covering the subsequent travel to China and Japan.

## Architecture & File Locations
- **Post Directory**: `content/posts/blizzcon-2026/`
- **Main Markdown File**: `content/posts/blizzcon-2026/index.md`
- **OCI Gallery Manifest**: `content/posts/blizzcon-2026/oci_manifest.json`

## Frontmatter Configuration
```yaml
---
title: "BlizzCon 2026"
date: 2026-10-02
description: "My trip to California for BlizzCon 2026."
summary: "My trip to Anaheim, California for BlizzCon 2026."
tags: ["Travel", "California", "BlizzCon", "Gaming"]
---
```

## Content Layout & Narrative Structure
The post follows the existing blog convention seen in `europe-2026` and `japan-2026`:

1. **Header Lead & Introduction**:
   - `{{< lead >}}` block indicating the date range.
   - Introductory paragraph establishing the setting: Southern California warmth, gathering with friends in Anaheim, and anticipation for BlizzCon announcements and community events.

2. **Day Breakdown (4 Days)**:
   - **Day 1: Arrival & SoCal Touchdown**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_1" >}} {{< /gallery >}}`
     - Focus: Flight into California, check-in near Anaheim Convention Center, badge pickup, grabbing regional food (e.g., In-N-Out).
   - **Day 2: BlizzCon Day 1 – Keynotes & Main Floor Exploration**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_2" >}} {{< /gallery >}}`
     - Focus: Morning line rush, opening ceremonies, game announcements, exploring convention hall demo stations and merch booths.
   - **Day 3: BlizzCon Day 2 – Esports, Cosplay & Community**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_3" >}} {{< /gallery >}}`
     - Focus: Community showcases, cosplay contests, tournament stages, evening social dinners/drinks.
   - **Day 4: Wrap-up & Transition Across the Pacific**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_4" >}} {{< /gallery >}}`
     - Focus: Decompressing, recovery brunch/coffee with the crew, packing bags, and closing with a narrative bridge leading directly to the China & Japan trip.

3. **OCI Gallery Manifest Integration**:
   - A placeholder `oci_manifest.json` file initialized to `{}` will be created in the post directory.
   - Ready for population by the site's `ocisync.py` script once bucket uploads are configured.

## Verification
- Run `hugo server --dryRun` or `hugo --gc` to verify that Hugo successfully parses the new post and frontmatter without build errors or missing shortcode warnings.
