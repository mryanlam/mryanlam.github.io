# China & Japan 2026 Post Design Specification

## Overview
This specification defines the structure, metadata, and scaffolding for the blog post covering the trip across Japan and China from September 14 to September 29, 2026. The post captures a 15-day itinerary: an initial Tokyo stopover, flying to Shanghai, a wedding in Jiaxing, exploring Beijing, returning to Japan for Osaka and Tokyo, and flying home through Vancouver and Seattle to Newark (EWR).

## Architecture & File Locations
- **Post Directory**: `content/posts/china-japan-2026/`
- **Main Markdown File**: `content/posts/china-japan-2026/index.md`
- **OCI Gallery Manifest**: `content/posts/china-japan-2026/oci_manifest.json` (initialized to `{}`)
- **Local Staging Directory**: `2026_china_japan/` with `day_1` through `day_15` subdirectories (ignored by git)

## Frontmatter Configuration
```yaml
---
title: "China & Japan 2026"
date: 2026-10-02
description: "Two weeks across Japan, Shanghai, Jiaxing, Beijing, and back."
summary: "A two-week adventure across Japan and China: Tokyo stopover, Shanghai & Jiaxing wedding, Beijing exploration, an extended Japan return, and flying home via Canada."
tags: ["Travel", "Japan", "China"]
---
```

## Content Layout & Narrative Structure
The post follows the existing blog convention (`europe-2026`, `japan-2026`, `blizzcon-2026`):

1. **Header Lead & Introduction**:
   - `{{< lead >}}` block: `Monday Sep 14, 2026 — Tuesday Sep 29, 2026`
   - Introduction setting the scene: taking off from LAX across the Pacific, a fast stopover in Tokyo, crossing into China for Shanghai street food, a modern wedding in Jiaxing, the history and scale of Beijing, followed by an extended return to Japan spanning Osaka and Tokyo before a multi-stop transpacific flight home.

2. **Detailed Narrative Days (Days 1–5)**:
   - **Day 1 (Tuesday Sep 15): Narita Touchdown & The Midnight Skyliner Dash**
     - Fast-track through Narita immigration with empty lines.
     - Missing the Narita Express due to earlier 6-hour LAX flight delays; taking the late Keisei Skyliner to Nippori and transferring to the Yamanote Line.
     - Checking into Shibuya Stream at 11:30 PM and crashing.
   - **Day 2 (Wednesday Sep 16): Shibuya Rain, Sweet Potato Frappes & Solo Leveling**
     - Early 5 AM jet lag wake-up, doing laundry on the 11th floor of Shibuya Stream.
     - Downstairs Starbucks breakfast in the rain: trying the sweet potato frappe (decaf surprise) and chocolate banana donut; heading up to the Google 35th-floor office coffee bar for real espresso.
     - Arcades, Mega Donki shopping, Tokyu Plaza soba lunch.
     - Visiting the Solo Leveling anime exhibition at Tokyu Plaza.
     - Afternoon hotel nap, followed by rain-free shabu shabu dinner connected through Shibuya Scramble.
   - **Day 3 (Thursday Sep 17): Haneda T2 to Shanghai & East Nanjing Road**
     - Morning check-out at 7 AM, heading to Haneda before rush hour.
     - Power Lounge Premium in Terminal 2 International (ANA flight out of T2); breakfast curry, karaage, and fish.
     - Flight to Shanghai, smooth visa stamping, phone data working seamlessly.
     - Shanghai Metro into the city (baggage scanners and tap-to-pay convenience), hotel upgrade to river view room.
     - Meeting up with Chiping and Abdul on East Nanjing Road pedestrian street.
     - Ah Ma's Handmade mochi tea, McDonald's fried salmon/shrimp burger, Chagee tea, and food court dinner.
   - **Day 4 (Friday Sep 18): The Bund, Crab Roe Noodles & Shanghai Street Food Tour**
     - Diverse hotel breakfast buffet; morning walk along the Bund and East Nanjing Road.
     - The infamous Luckin Coffee orange juice coffee misadventure.
     - Custom shirt at the Jordan store; meeting Abdul at West Nanjing Road for crab roe noodles and crab xiao long bao.
     - Exploring Shanghai Book World and picking up a G.E.M. album; scoring the Shanghai-exclusive Adidas jacket in Pudong.
     - Evening Shanghai food tour led by Tony with fellow travelers and unexpected Google colleagues from the same building, dining on XLB, sheng jian bao, scallion oil noodles, braised pork belly, and desserts.
   - **Day 5 (Saturday Sep 19): Jade on 36, High-Speed Rail to Jiaxing & The Wedding**
     - Morning gym workout on the 4th floor; French lunch special at Jade on 36 using hotel credits.
     - Meeting Abdul at Shanghai Hongqiao Station for the high-speed train to Jiaxing.
     - Checking into Jiaxing hotel via DiDi, changing into formal wear for Chiping & Ning's wedding.
     - Experiencing a modern Chinese wedding with stage MC, game-show raffles, prizes, and banquet courses.

3. **Scaffolded Days (Days 6–15 with Placeholders & Gallery Shortcodes)**:
   - **Day 6 (Sunday Sep 20): Journey North to Beijing**
   - **Day 7 (Monday Sep 21): Exploring Beijing – Day 1**
   - **Day 8 (Tuesday Sep 22): Exploring Beijing – Day 2**
   - **Day 9 (Wednesday Sep 23): Flight to Japan: Touching Down in Osaka**
   - **Day 10 (Thursday Sep 24): Osaka Adventures – Day 1**
   - **Day 11 (Friday Sep 25): Osaka Adventures – Day 2**
   - **Day 12 (Saturday Sep 26): Shinkansen from Osaka to Tokyo**
   - **Day 13 (Sunday Sep 27): Back in Tokyo**
   - **Day 14 (Monday Sep 28): Departure from Tokyo: Vancouver & Seattle Layovers to the Redeye**
   - **Day 15 (Tuesday Sep 29): Redeye Arrival: Morning Touchdown at EWR**

4. **Gallery Shortcode Standard**:
   - Each day contains `{{< gallery >}} {{< oci_gallery day="day_X" >}} {{< /gallery >}}`.

## Verification
- Validate with `hugo --printPathWarnings --gc` to ensure 0 build errors and proper template rendering.
