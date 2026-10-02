# BlizzCon 2026 Post Design Specification

## Overview
This specification defines the structure, metadata, and content outline for the blog post covering the trip to California for BlizzCon 2026. Following the decision to split the overall journey into two separate posts, this post focuses on the Anaheim/BlizzCon convention leg (Friday to Monday departure), ending with boarding the transpacific flight at LAX. The landing in Tokyo will kick off the subsequent China & Japan trip post.

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
summary: "Four days in Anaheim for BlizzCon 2026: Classic+ dungeon demos, dev meetups, and a 6-hour LAX delay."
tags: ["Travel", "California", "BlizzCon", "Gaming"]
---
```

## Content Layout & Narrative Structure
The post follows the style and structure seen in `europe-2026` and `japan-2026`:

1. **Header Lead & Introduction**:
   - `{{< lead >}}` date range block.
   - Narrative opening setting the stage: heading out to Southern California for BlizzCon, linking up with friends in Anaheim, diving headfirst into World of Warcraft Classic+ demos, and surviving the chaos of LAX.

2. **Day Breakdown (4 Days)**:
   - **Day 1 (Friday): LAX Arrival, Badge Pickup & Sabrosada**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_1" >}} {{< /gallery >}}`
     - Storyline: American Airlines flight with surprising free food; meeting up with Tater at LAX; navigating the peculiar layout to LAX-it for a ride to Anaheim; checking into the Hilton; picking up badges at the convention center (including Tenju's after getting him to text an ID photo); Tenju arriving and parking; late-night dinner at Sabrosada Mexican food.
   
   - **Day 2 (Saturday): BlizzCon Day 1 – Sprawling Lines, Classic+ Demos & The Shark Hazard**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_2" >}} {{< /gallery >}}`
     - Storyline: Early morning wake-up into a massive, winding entrance line; attempting to watch the opening ceremony with Vynestra, Leyna, and friends in Diablo Immortal before moving to WoW due to AV issues; hyping the StarCraft & Warcraft trailers before jumping into the demo line; struggling as a nerfed Frost Mage in the Classic+ dungeon; debriefing with Mael before his meet-and-greet; pho lunch nearby; leveling demo run to level 4 with Tenju; panels; evening 3-player dungeon run tanking on Prot Paladin (clearing an extra boss before dying to the shark); dinner with Mael at Cheesecake Factory learning the shark was an environmental hazard without loot.

   - **Day 3 (Sunday): BlizzCon Day 2 – Sarthe's Talent Hack, Quesabirria & Bottle Rocket**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_3" >}} {{< /gallery >}}`
     - Storyline: Morning demo run with Vynestra and Ashler (downing 3 bosses); attending developer panels featuring Mael and Aggrend; convention center lunch of quesabirria quesadillas, horchata float, and cantaloupe agua fresca; catching Sarthe's online tip about using legacy talents for capstone abilities; afternoon demo run with a PUG tanking on Prot Warrior (clearing 3 bosses easily, running out of time on the 4th); evening dinner and drinks at Bottle Rocket with Coup, Aggrend, Mael, Ashler, Helt, and crew with food truck grub.

   - **Day 4 (Monday): Anaheim Rush Hour, A 6-Hour LAX Delay & Heading West**
     - Gallery shortcode: `{{< gallery >}} {{< oci_gallery day="day_4" >}} {{< /gallery >}}`
     - Storyline: Morning Starbucks run downstairs; navigating morning rush hour and Tenju's confusing scenic route to LAX; checking in and enjoying a boozy lounge brunch (rum and coke hitting strong); rolling departure delays turning into a 6-hour wait; bouncing between lounge and gate; second round of lounge dinner; boarding the long-haul flight across the Pacific and getting some rest, setting the stage for landing in Tokyo in the next post.

3. **OCI Gallery Manifest Integration**:
   - `oci_manifest.json` initialized to `{}` in `content/posts/blizzcon-2026/`.
   - Ready for image synchronization via `ocisync.py`.

## Verification
- Validate the post with `hugo server --dryRun` or `hugo --gc` to verify formatting, frontmatter, and shortcode rendering without errors.
