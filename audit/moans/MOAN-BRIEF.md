# MOAN BRIEF — sửa tiếng rên H-scene theo quy tắc romaji

Standing brief for moan-fix agents. Read this + `~/workspace/maitetsu-pilot/AUDIT-BRIEF.md` + `~/workspace/custom-skills/aligned_translation_audit/SKILL.md` before starting. Sources (durable, NEVER /tmp): `~/workspace/maitetsu-pilot/sources/toml2/` (227 TOML files, #U-escaped filenames on disk) and `~/workspace/maitetsu-pilot/sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv` (91,731 rows). CSV3 File column uses SINGLE backslashes — use `r['File'].split(chr(92))[-1]`. TOML files are UTF-8 BOM + CRLF — preserve both. When a file has 2 CSV sets, audit ONLY the good set (verify by VN flat-match against the TOML; see `~/workspace/maitetsu-pilot/dual-csv-sets.md`).

## Scope — moans ONLY

Fix ONLY moan / breath / gasp / SFX renderings in this ONE H-scene file. Do NOT fix pronouns, terminology, meaning errors, misalignments, or anything else — those belong to the audit loop / unification pass. If a moan row is ALSO misaligned or untranslated, flag it (do not fix it here).

What counts as a moan row: any row whose JP contains a moan/breath/gasp/SFX sound — っ gasps, ふぁ/ふあ/ふぇ/ふや family, ひあ/ひゃ family, あ/は/ん/く/ふ sounds, laughter (ふふっ/うふふ/んふふ), long vowels (う/ぅ chains), SFX in （ ） or 「 」, and any VN that renders such a sound (Ư, phà/phùa, Hự, Kua, Kh, Fufu, etc.).

## Rules (all decided, in force)

1. **Spontaneity (Hieu 19/11 22:05):** moans/breaths/laughter rendered SPONTANEOUSLY per character + context. SFX tables are DEFAULTS only. Giggles (ふふっ/うふふ/んふふ) are LAUGHTER, never gasps.
2. **Japanese-faithfulness (Hieu 19/11 22:19):** default to staying as close to Japanese as possible; switch to pure Vietnamese ONLY when the Japanese-faithful rendering sounds too awkward.
3. **ROMAJI FALLBACK (Hieu approved 21/11 ~01:56):** when a Vietnamese rendering of a moan/breath sounds ngượng (forced/cringey) — especially long multi-vowel moans and the fa/fu family ("phà"/"phùa") and ひあ/ひゃ family — use the romaji of the JP sound instead (Hepburn, matching JP sound shape; vowel length per the vowel formula), e.g. ふあぁ→"Fuaa", ひゃぁ→"Hyaa". One row = ONE rendering (Vietnamese OR romaji, never mixed).
3b. **ひゃ/ひゅ/ひあ/きゃ → ROMAJI in moan rows (decided 21/11 ~11:55 by parent per Hieu's delegation "tôi để bạn tự đánh giá", evidence from 12 merged moan files):** "Á" for ひゃ/ひゅ/ひあ/きゃ is a SOUND-LOSS error — it drops the mora consonant hy-/ky- entirely (precedent ポーレットh3: "'Á' cho きゃっ/ひゃっ/やっ" listed as lost-consonant error; 凪h2 corrected ひあ "Hya"→"Hia" in 5 rows; んひゅ→"Nhyu/Nhyun" in h7 836/837, 稀咲h3 2277, 凪h2 2512). Render: ひゃ→"Hya", ひゅ→"Hyu", ひあ→"Hia", きゃ→"Kya", んひゅ→"Nhyu", んひゅん→"Nhyun" (vowel length per the formula; trailing っ on a short romaji moan is implicit, add !/? only when JP has them). "Á" stays correct ONLY when JP has no mora consonant (あっ/あぁ). The 20/11 spontaneity rule for this family now governs HOW the romaji is shaped per character/context (length, punctuation), not whether to use "Á". Garbled speech (e.g. ひっはひ/ひょはひょひょ with mouth full) is NOT a moan row — leave to audit.
4. **Ư for lost gasps STAYS (locked):** っ → Ư when the sound would otherwise be completely lost; NEVER double-render an already-rendered っ. Do NOT revisit the 1,146 gasp-sweep Ư rows. "Kh" for glottal-stop っ KEEPS (decided 21/11 — sound already rendered as a choked "Kh"; e.g. ふかみh2 989/997/1017/1731/1739).
5. **fa/fu LOCKED (with romaji exception):** ふぁ/ふあ → "phà"/"phùa", ふぇ → "phuê", ふやぁ → "phuya" — UNLESS the Vietnamese rendering sounds ngượng in that row, in which case use romaji (rule 3). Never "phá"/romanisation of a different sound.
6. **Vowel-length formula:** VN vowel count = 1 + number of う/ぅ in JP. Applies to romaji too (count the romaji vowels the same way).
7. **JP beats TW** when they disagree. Original VN was by Gemini and frequently fabricates — check every row against JP.
8. **NO bulk script fixing (Hieu 19/11):** scripts ONLY for enumeration/counting, assembling TOML blocks from hand-written fix values, and mechanical verification. Every fix hand-written from reading that row's JP (+TW). Mandatory FULL second read-through pass of every fix value vs its JP; review must state second-pass counts (total / re-verified / removed / corrected).

## Method per file

1. Read EVERY row of the file in CSV3 (good set only) + TOML-2. List every moan row (JP sound + TW + old VN).
2. For each moan row, judge: is the old VN rendering (a) correct and natural — KEEP; (b) wrong sound/meaning — FIX with the correct rendering; (c) correct sound but ngượng in Vietnamese — FIX with romaji (rule 3).
3. Check the sweep: read `sweep-raw-gasp-wrong.json` DIRECTLY for this file's gasp entries (the sweep itself has errors — verify each entry against its own exclusion rule before trusting it).
4. Check cross-file consistency only for the moan rows you touch (project VN index) — do not re-audit the file.

## Deliverables (in `~/workspace/maitetsu-pilot/moans/`)

- `moan-<slug>-REVIEW.md` — ends with "Kết bài". Sections: file verification (TOML md5, CSV good set, rows), moan inventory (how many moan rows, by kind), per-row fix sections (JP / TW / old VN / new VN / reason), kept-moan notes (renderings you judged correct, with 1-line reasons for the notable ones), flags (rows you could not decide — with full context), second-pass counts, TOML block.
- `moan-<slug>-wrong.json` — standard list-of-dicts shape: key as STRING, jp, tw, old_vn, fix, kind, character. Only rows you CHANGE go here.
- `moan-snippet-<slug>.md` — one-line-per-fact summary + totals line: `**Tổng cộng sau file này: N file / M dòng sai (moan)**` with the base = CURRENT `moans/ROUTE-MOANS.md` total (rebase if stale — never trust your spawn-time base).
- Agents do NOT edit `moans/ROUTE-MOANS.md` — the loop parent merges and REBASES totals.
- NEVER send files to Hieu; results in chat only (via the loop report).
