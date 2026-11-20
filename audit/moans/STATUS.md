# Moan-fix status — H-scene tiếng rên (romaji fallback)

Task created 21/11 ~02:00 by Hieu: "sửa tiếng rên toàn bộ H scene theo quy tắc romaji" (romaji fallback approved 21/11 ~01:56 — use romaji when the Vietnamese rendering sounds ngượng).

## Scope

- **58 unique H-files** project-wide (59 TOML files; lr_稀咲ポーレットh1 is duplicated).
- **Queue now: 20 files** — H-files already merged in ROUTE-AUDIT.md (audited BEFORE the romaji rule existed). Ordered by audit wrong-count desc (see `queue.md` / `queue.json`).
- **39 files not yet merged** in the audit loop — they join this queue automatically when merged (loop re-scans ROUTE-AUDIT.md each run). Future audits already apply the romaji rule (AUDIT-BRIEF.md), so those files should need only a light moan check.

## Rules

- Moans ONLY (see `MOAN-BRIEF.md`). No pronoun/terminology/meaning fixes here.
- Fixes are amendments — applied with the unification pass (after all 216 audits finish), NOT by editing TOML directly now.
- Ư gasp rows are NOT revisited. "Kh" for glottal-stop っ KEEPS.
- Report in Vietnamese on every loop run. Commit to GitHub after every merge (same snapshot procedure as the audit loop; moan files push as `audit/moans/*`).

## Totals

- **2 / 20 files moan-fixed, 38 rows changed** (merged 21/11 ~02:31: ふかみh1 13 + 凪h2 25; loop started 21/11 ~02:14).
- 02:14 21/11 (run 1): spawned first 2 moan-fix agents — ふかみh1_ともはり練習 (272 rows) and 凪h2_おとなの水着 (673 rows). Re-scan found no new H-files in ROUTE-AUDIT.md (20/20 already in queue).
- Loop: `maitetsu-moan-fix-loop`, every 30 min, owner goal:maitetsu-last-run-vietnamese-localization. Stops itself when all H-files are merged AND moan-fixed.
