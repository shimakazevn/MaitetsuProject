# Rules for Maitetsu Last Run!! Translation Project

## Patch Packaging Rules
* The output patch archive MUST be named exactly `patch3.xp3`. DO NOT rename it to `patch_vn.xp3` or `patch_data3.xp3` or any other name.
* To ensure `patch3.xp3` has the highest priority and overrides files inside `patch_data2.xp3` (which is loaded after `patch3.xp3` due to alphabetical ordering), we use a custom `custom.tjs` file located at `vn_patch/custom.tjs`.
* `vn_patch/custom.tjs` has been modified to include the following re-mounting line at the very top:
  `Storages.addAutoPath(System.exePath + "patch3.xp3>");`
  This ensures `patch3.xp3` is dynamically re-mounted at runtime with the absolute highest priority.

## Translation Source & Quality Rules
* **Translate from Japanese**: To guarantee maximum translation accuracy, avoid double-translation errors, and ensure alignment with the spoken Japanese voiceovers, always translate from the original Japanese source text (found in code comments, file names, or Japanese original files).
  * **For TIPS**: For each Chinese TIPS file `tw_tips_<name>.txt`, load the corresponding Japanese original file `tips_<name>.txt` located in `KrkrExtract_Output/data/scenario/tips/` and translate directly from the Japanese text. Use the Chinese file only for structure.
* **Chinese as Structural Template only**: Use the Traditional Chinese version files (`_tw`, `tw_tips_*.txt`, `scnlist_tw.tjs`, `soundlist_tw.csv`) strictly as file structural templates to preserve engine and font compatibility. Do not translate directly from Chinese unless Japanese source text is unavailable.
* **Keep Engine Labels Untranslated**: Anchor labels such as `*解説` must remain exactly as-is. Character speaker brackets must remain as full-width brackets `【` and `】`.

## Project References & Documents
* **[Walkthrough History](file:///E:/まいてつ Last Run!!/.agents/walkthrough.md)**: A detailed log of changes and patches applied during this session.
* **[TIPS Translation Context Glossary](file:///E:/まいてつ Last Run!!/.agents/context_trans.md)**: The full bilingual glossary (Traditional Chinese ➔ Vietnamese) for the translated TIPS terms.


