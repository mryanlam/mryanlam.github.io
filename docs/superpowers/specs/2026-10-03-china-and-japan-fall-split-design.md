# China 2026 & Japan Fall 2026 Two-Post Refactor Design Specification

## Overview
This specification details refactoring the unified 15-day China/Japan post into two distinct, chronological posts corresponding to the natural two-week itinerary:
1. **Week 1: China & The Tokyo Stopover 2026 (`china-2026`)** — Mon Sep 14 to Wed Sep 23 (~9 days)
2. **Week 2: Japan Fall 2026 (`japan-fall-2026`)** — Wed Sep 23 to Tue Sep 29 (~7 days)

This eliminates the awkward "sandwich" jump, keeps both posts strictly chronological and bite-sized, and avoids slug collision with the existing winter `japan-2026` post.

## Post 1: China & The Tokyo Stopover 2026

### File Locations
- **Post Directory**: `content/posts/china-2026/`
- **Markdown Index**: `content/posts/china-2026/index.md`
- **OCI Gallery Manifest**: `content/posts/china-2026/oci_manifest.json` (initialized as `{}`)
- **Local Staging Directory**: `2026_china/` (containing `day_1` through `day_9`, ignored by Git)

### Frontmatter
```yaml
---
title: "China & The Tokyo Stopover 2026"
date: 2026-10-02
description: "A week across Tokyo, Shanghai, Jiaxing, and Beijing."
summary: "Week 1 of my Asia trip: A quick stopover in Tokyo, crossing into China for Shanghai street food, a friend's wedding banquet in Jiaxing, and exploring Beijing before flying out to Osaka."
tags: ["Travel", "China", "Japan"]
---
```

### Day Breakdown (9 Days)
- `{{< lead >}}` Monday Sep 14, 2026 — Wednesday Sep 23, 2026 `{{< /lead >}}`
- **Day 1 (Sep 15): Narita Touchdown & The Midnight Skyliner Dash** (Full narrative)
- **Day 2 (Sep 16): Shibuya Rain, Sweet Potato Frappes & Solo Leveling** (Full narrative)
- **Day 3 (Sep 17): Haneda T2 to Shanghai & East Nanjing Road** (Full narrative)
- **Day 4 (Sep 18): The Bund, Crab Roe Noodles & Shanghai Street Food Tour** (Full narrative)
- **Day 5 (Sep 19): Jade on 36, High-Speed Rail to Jiaxing & The Wedding** (Full narrative)
- **Day 6 (Sep 20): Journey North to Beijing** (Placeholder scaffold)
- **Day 7 (Sep 21): Exploring Beijing – Day 1** (Placeholder scaffold)
- **Day 8 (Sep 22): Exploring Beijing – Day 2** (Placeholder scaffold)
- **Day 9 (Sep 23): Flight Out of Beijing to Osaka** (Bridge to Japan Fall 2026)

---

## Post 2: Japan Fall 2026

### File Locations
- **Post Directory**: `content/posts/japan-fall-2026/`
- **Markdown Index**: `content/posts/japan-fall-2026/index.md`
- **OCI Gallery Manifest**: `content/posts/japan-fall-2026/oci_manifest.json` (initialized as `{}`)
- **Local Staging Directory**: `2026_japan_fall/` (containing `day_1` through `day_7`, ignored by Git)

### Frontmatter
```yaml
---
title: "Japan Fall 2026"
date: 2026-10-02
description: "A week in Osaka and Tokyo, and the long journey home."
summary: "Week 2 of my Asia trip: Touching down in Osaka fresh from Beijing, bullet training back to Tokyo, and heading home via Vancouver and Seattle."
tags: ["Travel", "Japan"]
---
```

### Day Breakdown (7 Days)
- `{{< lead >}}` Wednesday Sep 23, 2026 — Tuesday Sep 29, 2026 `{{< /lead >}}`
- **Day 1 (Sep 23): Touching Down in Osaka from Beijing** (Placeholder scaffold)
- **Day 2 (Sep 24): Osaka Adventures – Day 1** (Placeholder scaffold)
- **Day 3 (Sep 25): Osaka Adventures – Day 2** (Placeholder scaffold)
- **Day 4 (Sep 26): Shinkansen from Osaka to Tokyo** (Placeholder scaffold)
- **Day 5 (Sep 27): Returning to Tokyo Favorites** (Placeholder scaffold)
- **Day 6 (Sep 28): Departure from Tokyo: Vancouver & Seattle Layovers to the Redeye** (Placeholder scaffold)
- **Day 7 (Sep 29): Redeye Arrival: Morning Touchdown at EWR** (Placeholder scaffold)

---

## Git & Clean-up Operations
- Remove deprecated `content/posts/china-japan-2026/` directory.
- Remove deprecated staging directory `2026_china_japan/`.
- Update `.gitignore` to replace `/2026_china_japan/` with `/2026_china/` and `/2026_japan_fall/`.
- Verify with `hugo --printPathWarnings --gc` that both new posts render without errors.
