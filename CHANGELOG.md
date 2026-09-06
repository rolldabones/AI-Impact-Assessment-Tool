# CHANGELOG.md

All notable changes to this repository. Versions follow semantic versioning. Prior versions are superseded upon release of the next.

Maintenance note (2026-07-14): a stale draft block duplicating the [1.2.1] entry and carrying an inaccurate [1.2.0] writeup (it described a SPEC.md that was never shipped) was removed from the top of this file. The retained [1.2.0] entry reflects the files actually released.

## [1.2.6] - 2026-09-06

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- **Doctrine citation line added** to the Part of the ecosystem section. This repository restates a doctrine and cited DOCTRINE.md nowhere, which is the Class E2 finding the new guards report.
- **Lockstep lag corrected, second occurrence.** The closing status line read `v1.2.2` against a masthead of `v1.2.5`, three patch releases behind. Found by reading in Session C, not by any guard. The new Class E4 reporter now names every version token in a README that differs from the masthead.
- **Informed Intent compression replaced with a pointer to the canon**, in `README.md` and in `INSTRUCTIONS-EXTENDED.md`. The superseded four-item compression (`purpose, scope, limits and a named owner`) matched neither limb of DOCTRINE.md v1.1.0 and is registered as superseded. `INSTRUCTIONS.md` is a production mirror and is unchanged; it carries a third compression of the same doctrine and is reported, not edited.
- All other files in this repository are unchanged byte for byte.

## [1.2.5] - 2026-08-13

OJ text of the amending regulation obtained; Article 5 date corrected.

**Correction, not a currency update.** The release earlier today stated that the Article 5 application date of 2 February 2025 was "settled and not affected by the Omnibus". Having now read the Official Journal text, that is **wrong in part** and is corrected here.

- **The amending act is identified.** Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026, OJ L, 2026/1744, 24.7.2026, ELI http://data.europa.eu/eli/reg/2026/1744/oj, in force 27 July 2026. Article 1, point (40) amends the third paragraph of Article 113 of Regulation (EU) 2024/1689.
- **The pinpoint question is answered.** Article 113 is structured in unnumbered paragraphs with lettered points. The correct citation form is **"Article 113, third paragraph, point (c)"**. "Article 113(3)" is wrong and always was. The prohibition on that form, adopted this morning as a precaution, is now replaced by a positive rule.
- **Article 5 carve-out.** Amended point (a) provides that Chapters I and II apply from 2 February 2025 **with the exception of Article 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b), which apply from 2 December 2026**. The general Article 5 date stands; the prohibitions the Omnibus added are deferred. The earlier unqualified statement is struck.
- **High-risk deferrals, verbatim.** Amended point (c): Chapter III, Sections 1, 2 and 3, with the exception of Article 6(5), apply from (i) 2 December 2027 for AI systems classified as high-risk pursuant to Article 6(2) and Annex III, and (ii) 2 August 2028 for those classified pursuant to Article 6(1) and Annex I.
- **New point (d).** Articles 102 to 110 apply from 27 July 2026.
- The OJ-text gap flag is removed from every file that carried it. That outstanding item is closed.

## [1.2.4] - 2026-08-13

License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## [1.2.3] - 2026-08-13

Omnibus currency remediation. The Digital Omnibus on AI entered into force on 27 July 2026; notes that described Official Journal publication as pending are recast as operative law with dated amendment notes. The Article 5 application date of 2 February 2025 is stated as fact (Article 113, point (a), Article 5 sitting in Chapter II), resolving one of the standing counsel Unknowns. No pinpoint to a numbered subsection of Article 113 is given: the amending regulation's Official Journal text has not been read and its renumbering is unconfirmed, so the consolidated text is cited with an as-at date and the gap is flagged in the file.

- README.md: regulatory currency paragraph recast with a dated amendment note; a scope paragraph added stating that the Assistant supports an impact assessment and does not perform a conformity assessment, issue a declaration of conformity or discharge any regulator-facing obligation.
- CROSSWALK.md: regulatory currency note re-headed as at 13 August 2026 and recast; a coverage-boundary paragraph added on the same point; sources repointed to the consolidated text on EUR-Lex and the Commission AI Act Service Desk reproduction of the Official Journal text of 13 June 2024.
- BUILD-GUIDE.md: broken link to SPEC.md repointed to INSTRUCTIONS-EXTENDED.md. SPEC.md does not exist in this repository.
- INSTRUCTIONS.md unchanged. It is the production mirror of the deployed instruction set and is not edited outside a redeployment.

## [1.2.2] - 2026-07-30

### Fixed
- Two occurrences of a find-and-replace failure in which the filename INSTRUCTIONS.md had been overwritten by its own description. Quickstart step 1 read "Copy the instruction block from  The full instruction block (v1.1.0) plus acceptance checklist into your platform's..." and the Files table row carried the same description in both cells with no link. Both now read INSTRUCTIONS.md as a working link. The file itself was always present; only the references were broken.
- The stale "(v1.1.0)" version reference inside those descriptions removed rather than updated, since the Files table describes the file and does not version it. INSTRUCTIONS.md states its own version.

### Changed
- Trademark rendering corrected to the canonical closed-up form GRCnext™. The retired spaced form "GRC next" is withdrawn from repository prose. One occurrence, in the grc line of the Part of the ecosystem section.
- Version and status lines updated in lockstep.

## [1.2.1] - 2026-07-13

### Changed
- INSTRUCTIONS.md deployed block mirrors two editorial edits made in the live GPT: capital L in both "Final Liability rests with the Human." closing lines, and the third doctrine label reverted from "Human accountability" to Final Liability (block now 7,599 characters; no behavioral change)
- README.md, BUILD-GUIDE.md and CROSSWALK.md versions aligned to 1.2.1

### Superseded
- v1.2.0 INSTRUCTIONS.md block

## [1.2.0] - 2026-07-13

### Added
- INSTRUCTIONS-EXTENDED.md: uncompressed long form retained for platforms without the Instructions box limit

### Changed
- INSTRUCTIONS.md now carries the deployed production block verbatim (7,604 characters, compressed for the GPT builder): adds the residual-risk evidence rule (planned controls do not reduce residual risk), a five-value decision taxonomy with conditions precedent vs subsequent, MODE declaration across six modes, default strictness (risk-averse enterprise), precise four-status evidence definitions, expanded RACI with "Unassigned: decision blocker" and a pre-output self-check
- Ten-item checklist split into two instruments: the Assistant's in-tool acceptance checklist (rates the assessed system) and the repo-side operator verification checklist (verifies the Assistant)
- README.md and BUILD-GUIDE.md updated for the two-file instruction structure and compression step
- CROSSWALK.md version aligned to 1.2.0 (content unchanged)

### Superseded
- v1.1.0 INSTRUCTIONS.md (long-form block as canonical)

## [1.1.0] - 2026-07-13

### Added
- INSTRUCTIONS.md: instruction block v1.1.0 with a ten-item acceptance checklist
- CROSSWALK.md: mapping to EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005, with a dated regulatory-currency note reflecting the 2026 Digital Omnibus on AI
- BUILD-GUIDE.md: the build log, split out of the README, corrected and updated
- CHANGELOG.md and LICENSE.md (CC BY-NC-SA 4.0)
- Ecosystem section linking the profile repository's canonical ECOSYSTEM.md and nearest-neighbor repositories

### Changed
- README.md rewritten: overview, audience, outputs, quickstart, file map, standards note, disclaimer, license
- Instruction block: added ISO/IEC 42005 alignment; added rule against reciting regulatory dates from memory; moved prohibited-use screen ahead of all scoring and added the NCII/CSAM prohibition; made the Threshold Gate deterministic (Consequence x Likelihood, worst domain governs); consolidated the v1 improvement round (evidence tags, system boundary, threat model, vendor controls, SLI/SLO monitoring, Decision Record, strictness modes) into the block itself; named the three doctrines and bound the DECISION step to Informed Intent; corrected NIST AI RMF function order to GOVERN, MAP, MEASURE, MANAGE
- Repository description made platform-agnostic (model choice noted as the reference implementation's, not a requirement)

### Fixed
- Grammatical and typographical errors in the build narrative ("The satisfaction condition should be whether", "You will likely be asked", "a GPT", "It finally completed")

### Superseded
- v1.0.0 README.md (single-file build log with embedded v1.0.0 prompt)

## [1.0.0] - initial release

- Single README.md containing the build narrative and the v1.0.0 instruction prompt

Final Liability rests with the Human.
