# China 2026 & Japan Fall 2026 Split Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor the unified China & Japan trip into two distinct, chronological blog posts in Hugo: `china-2026` (Week 1: Tokyo stopover & China, 9 days) and `japan-fall-2026` (Week 2: Osaka & Tokyo return, 7 days), with manifests, staging folders, and Hugo build verification.

**Architecture:** Two Hugo page bundles at `content/posts/china-2026/` and `content/posts/japan-fall-2026/`, with respective `oci_manifest.json` files and staging directories `2026_china/` and `2026_japan_fall/` ignored in `.gitignore`. Deprecate `content/posts/china-japan-2026/`.

**Tech Stack:** Hugo, Markdown, JSON, Bash, Git.

## Global Constraints
- Post 1: `content/posts/china-2026/index.md` and `content/posts/china-2026/oci_manifest.json`
- Post 2: `content/posts/japan-fall-2026/index.md` and `content/posts/japan-fall-2026/oci_manifest.json`
- Staging folders `2026_china/` and `2026_japan_fall/` ignored in `.gitignore`
- Deprecated `content/posts/china-japan-2026/` removed from repo
- Hugo build must pass cleanly with zero errors

---

### Task 1: Update .gitignore and Staging Folders

**Files:**
- Modify: `.gitignore`
- Create (untracked): `2026_china/{day_1..day_9}`
- Create (untracked): `2026_japan_fall/{day_1..day_7}`
- Delete: `2026_china_japan/`

**Interfaces:**
- Produces: Git-ignored staging folders for both posts ready for image drops.

- [ ] **Step 1: Update `.gitignore`**

Replace `/2026_china_japan/` with `/2026_china/` and `/2026_japan_fall/` in `.gitignore`.

- [ ] **Step 2: Create staging directories and remove old staging directory**

Run:
```bash
mkdir -p 2026_china/{day_1,day_2,day_3,day_4,day_5,day_6,day_7,day_8,day_9}
mkdir -p 2026_japan_fall/{day_1,day_2,day_3,day_4,day_5,day_6,day_7}
rm -rf 2026_china_japan
```

- [ ] **Step 3: Commit .gitignore**

```bash
git add .gitignore
git commit -m "chore: configure staging directories for china and japan-fall in gitignore"
```

---

### Task 2: Create China 2026 Post and Manifest

**Files:**
- Create: `content/posts/china-2026/oci_manifest.json`
- Create: `content/posts/china-2026/index.md`

**Interfaces:**
- Produces: Complete Week 1 post bundle for China & Tokyo Stopover 2026 with Days 1–9.

- [ ] **Step 1: Create `content/posts/china-2026/oci_manifest.json`**

Write:
```json
{}
```

- [ ] **Step 2: Create `content/posts/china-2026/index.md`**

Write:
```markdown
---
title: "China & The Tokyo Stopover 2026"
date: 2026-10-02
description: "A week across Tokyo, Shanghai, Jiaxing, and Beijing."
summary: "Week 1 of my Asia trip: A quick stopover in Tokyo, crossing into China for Shanghai street food, a friend's wedding banquet in Jiaxing, and exploring Beijing before flying out to Osaka."
tags: ["Travel", "China", "Japan"]
---

## China & The Tokyo Stopover 2026
{{< lead >}}
Monday Sep 14, 2026 — Wednesday Sep 23, 2026
{{< /lead >}}

The first week of an epic transpacific journey. Kicking off with an initial Tokyo stopover to decompress from flight delays and wander through rainy Shibuya, before crossing into China for high-speed trains, Shanghai street food, a modern wedding celebration in Jiaxing, and taking in the monumental scale of Beijing—all leading up to boarding a flight back to Japan.

### Day 1: Narita Touchdown & The Midnight Skyliner Dash
---
{{< gallery >}}
  {{< oci_gallery day="day_1" >}}
{{< /gallery >}}

After the massive six-hour delay back at LAX, our flight finally touched down at Narita Airport late in the evening. Stepping off the plane, I was greeted by an absolute travel miracle: the foreign passport immigration lines were completely deserted. I walked straight through without waiting a single minute.

Because of the severe flight delays, the Narita Express had already shut down for the night. Thinking fast, I pivoted over to the Keisei Skyliner, taking it into Nippori before transferring onto the Yamanote Line to Shibuya. I finally dragged my bags into the Shibuya Stream hotel and checked in at 11:30 PM. Running on pure fumes and jet lag, all I could do was collapse onto the bed and pass out.

### Day 2: Shibuya Rain, Sweet Potato Frappes & Solo Leveling
---
{{< gallery >}}
  {{< oci_gallery day="day_2" >}}
{{< /gallery >}}

Jet lag showed no mercy, waking me up bright and early at 5:00 AM. Since Shibuya Stream has a dedicated laundry room on the 11th floor, I took advantage of the pre-dawn hours to get a full load of laundry washed and folded.

Stepping outside, the rain was coming down pretty heavily. I decided to pop into Starbucks downstairs for breakfast, ordering a chocolate banana donut and a sweet potato frappe. The donut was solid, but the sweet potato drink was strange—and worse, I discovered too late that it was completely caffeine-free. Needing an actual caffeine fix to start my day, I headed up to the Google office on the 35th floor to rescue myself with a proper espresso from the coffee bar.

Fully awake, I ducked into local arcades and wandered through MEGA Donki for some shopping. For lunch, I found a comforting soba restaurant inside Tokyu Plaza, then headed upstairs in the same building to check out the Solo Leveling anime exhibition. The walkthrough featured impressive art and full-scale sculptures from the series. After another stroll through the rain, exhaustion caught up with me and I headed back to the hotel for an afternoon reset nap.

For dinner, I stayed dry by walking through the indoor connection from the hotel into Shibuya Scramble mall, sitting down for a warm and satisfying shabu shabu meal.

### Day 3: Haneda T2 to Shanghai & East Nanjing Road
---
{{< gallery >}}
  {{< oci_gallery day="day_3" >}}
{{< /gallery >}}

Another early 5:00 AM wake-up call to pack up my luggage for the morning flight to Shanghai. After catching up on some Discord chats, I checked out around 7:00 AM to take the train over to Haneda Airport before the morning rush hour peaked.

At Haneda, I checked out the Power Lounge Premium in the Terminal 2 international section. Interestingly, ANA is the only airline operating international flights out of Terminal 2, which made navigating surprisingly smooth. The lounge spread hit the spot with breakfast curry rice, crispy karaage, grilled fish, and hot coffee.

The flight into Shanghai was smooth and uneventful. Passing through customs was quick, my visa was stamped without issue, and my mobile data connected immediately. I hopped onto the Shanghai Metro toward the city center—it was fascinating to see airport-style luggage scanners at the subway entrance, but the tap-to-pay convenience was effortless.

Upon arriving at my hotel, I was pleasantly surprised to receive an upgrade to a room with a fantastic river view. Chiping met me at the hotel, and together we headed over to East Nanjing Road pedestrian shopping street to link up with Abdul. We stopped by Ah Ma's Handmade for tea featuring handmade mochi instead of standard boba, and Chiping walked us through ordering at a Chinese McDonald's, where I tried a wild burger stacked with an egg, fried salmon, and fried shrimp. After browsing through various stores along the strip, we capped off the evening with a food court dinner of roasted chicken, vegetables, and more tea.

### Day 4: The Bund, Crab Roe Noodles & Shanghai Street Food Tour
---
{{< gallery >}}
  {{< oci_gallery day="day_4" >}}
{{< /gallery >}}

I kicked off the morning by taking full advantage of the extensive hotel breakfast buffet, which featured an impressive spread spanning traditional Chinese dishes, Indian specialties, Japanese bites, and Western staples. Fueled up, I took a scenic morning stroll along the iconic Bund and worked my way westward along East Nanjing Road.

Along the way, I got baited by anime store decor into ordering a Luckin Coffee with orange juice—a flavor combination that turned out to be truly vile. I cleansed my palate with some retail therapy, designing a custom shirt at the Jordan store.

Later on, I met up with Abdul on West Nanjing Road, and we sat down for an incredible lunch of rich crab roe noodles and crab xiao long bao. As light rain began to fall, we ducked into Shanghai Book World, an expansive multi-story bookstore with a dedicated music floor where I scored a G.E.M. vinyl/CD album. Heading back toward Pudong, I checked out a nearby mall and managed to find the coveted Shanghai-exclusive Adidas track jacket in my size.

In the evening, I joined a guided food tour led by Tony, an energetic guide who grew up in Korea and spent time living in Boston. The group was an international mix of Australians, Europeans, and Americans—and by pure coincidence, two other tour guests were also Googlers, with one of them (Ben) working in my exact same building! Together, we ate our way through Shanghai's culinary highlights: soup-filled xiao long bao, crispy pan-fried sheng jian bao, fragrant scallion oil noodles, curry noodles, tender braised pork belly, and sweet mango coconut desserts, capping the night off with drinks at a nearby bar.

### Day 5: Jade on 36, High-Speed Rail to Jiaxing & The Wedding
---
{{< gallery >}}
  {{< oci_gallery day="day_5" >}}
{{< /gallery >}}

Knowing a big food day was ahead, I kept breakfast light at the hotel and hit the 4th-floor gym for a strength training session to build up an appetite. For lunch, I used my hotel dining credits at Jade on 36, enjoying an exceptional French lunch special overlooking the city skyline.

After checking out, I reunited with Abdul at Shanghai Hongqiao Railway Station to catch the high-speed bullet train to Jiaxing for Chiping and Ning's wedding. Once in Jiaxing, we took a quick DiDi to our hotel, got checked in, and dressed up for the ceremony.

The wedding was an incredible spectacle—a modern Chinese celebration complete with a main stage, an energetic MC, and interactive game-show segments with audience raffles and prizes. Course after course of banquet dishes flowed to the tables throughout the festivities. After celebrating with the newlyweds and friends, we headed back to the hotel to rest up for our upcoming trip to Beijing.

### Day 6: Journey North to Beijing
---
{{< gallery >}}
  {{< oci_gallery day="day_6" >}}
{{< /gallery >}}

Traveling north from Jiaxing to the historic capital of Beijing, settling into our new base, and exploring the surrounding neighborhoods.

### Day 7: Exploring Beijing – Day 1
---
{{< gallery >}}
  {{< oci_gallery day="day_7" >}}
{{< /gallery >}}

First full day diving into Beijing's historic landmarks, architecture, and iconic local food.

### Day 8: Exploring Beijing – Day 2
---
{{< gallery >}}
  {{< oci_gallery day="day_8" >}}
{{< /gallery >}}

Continuing our exploration of Beijing, taking in the sights, culture, and bustling streets.

### Day 9: Departure from Beijing: Flight Out to Osaka
---
{{< gallery >}}
  {{< oci_gallery day="day_9" >}}
{{< /gallery >}}

Wrapping up our time in China, heading to the airport in Beijing, and boarding our flight across the sea to Osaka, Japan, to kick off Week 2 of the adventure!
```

- [ ] **Step 3: Commit**

```bash
git add content/posts/china-2026/
git commit -m "feat: add China & The Tokyo Stopover 2026 blog post and manifest"
```

---

### Task 3: Create Japan Fall 2026 Post and Manifest

**Files:**
- Create: `content/posts/japan-fall-2026/oci_manifest.json`
- Create: `content/posts/japan-fall-2026/index.md`

**Interfaces:**
- Produces: Complete Week 2 post bundle for Japan Fall 2026 with Days 1–7.

- [ ] **Step 1: Create `content/posts/japan-fall-2026/oci_manifest.json`**

Write:
```json
{}
```

- [ ] **Step 2: Create `content/posts/japan-fall-2026/index.md`**

Write:
```markdown
---
title: "Japan Fall 2026"
date: 2026-10-02
description: "A week in Osaka and Tokyo, and the long journey home."
summary: "Week 2 of my Asia trip: Touching down in Osaka fresh from Beijing, bullet training back to Tokyo, and heading home via Vancouver and Seattle."
tags: ["Travel", "Japan"]
---

## Japan Fall 2026
{{< lead >}}
Wednesday Sep 23, 2026 — Tuesday Sep 29, 2026
{{< /lead >}}

The second half of our Asia journey. Picking up right after our flight from Beijing, we touched down in Osaka for incredible street food, vibrant neighborhoods, and rhythm game sessions, before taking the Shinkansen bullet train back to Tokyo and navigating a multi-stop flight home via Canada.

### Day 1: Touching Down in Osaka from Beijing
---
{{< gallery >}}
  {{< oci_gallery day="day_1" >}}
{{< /gallery >}}

Arriving in Osaka on our flight from Beijing, clearing customs, checking into our hotel, and heading out into the evening streets for our first taste of Kansai flavors.

### Day 2: Exploring Osaka – Day 1
---
{{< gallery >}}
  {{< oci_gallery day="day_2" >}}
{{< /gallery >}}

Diving headfirst into Osaka's vibrant food scene, shopping arcades, and bustling city energy.

### Day 3: Exploring Osaka – Day 2
---
{{< gallery >}}
  {{< oci_gallery day="day_3" >}}
{{< /gallery >}}

Another full day soaking up Osaka's sights, arcades, and culinary highlights.

### Day 4: Shinkansen from Osaka to Tokyo
---
{{< gallery >}}
  {{< oci_gallery day="day_4" >}}
{{< /gallery >}}

Boarding the Tokaido Shinkansen bullet train eastward from Osaka to Tokyo, checking into our hotel, and returning to familiar city haunts.

### Day 5: Returning to Tokyo Favorites
---
{{< gallery >}}
  {{< oci_gallery day="day_5" >}}
{{< /gallery >}}

A full day in Tokyo enjoying favorite neighborhoods, shopping runs, arcade sessions, and reunion meals.

### Day 6: Departure from Tokyo: Vancouver & Seattle Layovers to the Redeye
---
{{< gallery >}}
  {{< oci_gallery day="day_6" >}}
{{< /gallery >}}

Saying goodbye to Tokyo, boarding the first transpacific flight, and navigating layovers and stopovers in Vancouver and Seattle before catching the cross-country redeye flight back to the East Coast.

### Day 7: Redeye Arrival: Morning Touchdown at EWR
---
{{< gallery >}}
  {{< oci_gallery day="day_7" >}}
{{< /gallery >}}

Touching down early in the morning at Newark Liberty International Airport (EWR), unpacking a suitcase full of memories, and concluding an unforgettable two-week journey across Japan and China.
```

- [ ] **Step 3: Commit**

```bash
git add content/posts/japan-fall-2026/
git commit -m "feat: add Japan Fall 2026 blog post and manifest"
```

---

### Task 4: Remove Obsolete Post & Verify Hugo Build

**Files:**
- Delete: `content/posts/china-japan-2026/`

- [ ] **Step 1: Remove deprecated `content/posts/china-japan-2026/`**

Run:
```bash
git rm -r content/posts/china-japan-2026
git commit -m "chore: remove deprecated china-japan-2026 unified post"
```

- [ ] **Step 2: Run Hugo build verification**

Run: `hugo --printPathWarnings --gc`
Expected: 0 errors, clean build.

- [ ] **Step 3: Verify both posts render in output**

Run:
```bash
test -f public/posts/china-2026/index.html && test -f public/posts/japan-fall-2026/index.html && echo "Both rendered successfully"
```
Expected: "Both rendered successfully"

- [ ] **Step 4: Cleanup public directory and check git status**

Run: `rm -rf public && git status`
Expected: Clean working tree.
