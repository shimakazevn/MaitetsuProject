# Audit — Maitetsu: Last Run!! Vietnamese localization

Row-by-row audit of the Vietnamese translation against the Japanese original
(+ the Taiwanese translation as a second opinion). Every audited file gets a
review (`audit-<slug>-REVIEW.md`, ends with "Kết bài"), a machine-readable
fix list (`audit-<slug>-wrong.json`), and a merge snippet
(`route-audit-snippet-<slug>.md`).

**Status (20/11/2026): 60 / 216 files audited, 3,335 lines wrong.**
`ROUTE-AUDIT.md` is the running log and totals chain. `audit-queue.md` is the
remaining work in severity order (strong-candidate count desc).
`AUDIT-BRIEF.md` is the standing brief every audit follows
(+ `~/workspace/custom-skills/aligned_translation_audit/SKILL.md`).

**Key rules:** no bulk scripts for fixing (scripts only enumerate / count /
verify); every fix hand-written from its JP row; mandatory full second pass;
JP beats TW when they disagree; results in chat only — no files are sent to
the translator unless asked. The っ-gasp sweep (`sweep-raw-gasp-*`, 1,146
fixed / 210 files) is a separate pass, cross-checked per file.

**Not in this folder:** the source data (227 TOML files + the CSV3 master,
51 MB) — kept in the Drive backup (`Maitetsu Last Run - Backup`) and in the
project workspace. The fixed TOML values live inside each review's TOML
block; the rebuild (applying fix lists + translating the last 2 untranslated
rows) happens after the audit + unification pass.
