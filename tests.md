# tests.md

**AI Impact Assessment Tool · tests · v1.6.0 · 25 November 2026 (KST)**

The tests for the instruction block in [INSTRUCTIONS.md](INSTRUCTIONS.md). This file holds the known defects, the critical cases and the record of logged runs. The cases, with their literal run inputs, are in [tests/prompt-cases.md](tests/prompt-cases.md).

## Cases

The suite is `aiia-v150`, twelve cases in [tests/prompt-cases.md](tests/prompt-cases.md), each with its literal run input. OV1 to OV10 are the ten items of the [Operator verification checklist](INSTRUCTIONS.md#operator-verification-checklist) in INSTRUCTIONS.md, with the run inputs of run R1; OV11 (repeatability) is scored jointly from the Threshold Gate tables of OV1, OV4 and OV10, whose run inputs are identical; OV12 tests the Informed Intent gate. The system prompt is the block followed by [DOCTRINE.md section 2](tests/system/doctrine-v1.2.5-section-2.md), verbatim, as README step 1 prescribes. Runs are made with [tests/run_prompt_cases.py](tests/run_prompt_cases.py) on `claude-opus-5-5` at max_tokens 32,000 and scored with [tests/score_prompt_cases.py](tests/score_prompt_cases.py) by `claude-sonnet-5-5`; both are published, so a run can be re-derived from this repository.

**Critical cases:** OV2, OV3, OV6, OV7 and OV12. Five cases are critical and seven are not.

Acceptance is read under the account rule, [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), from 26 October 2026; until then the rule here was that all ten must pass. The checklist verifies the Assistant itself; the Assistant's own ten-item acceptance checklist, inside the block, rates an assessed system and is case 9's subject, not a separate suite.

## Known defects

Recorded, not fixed, unless marked closed. Each open defect is a change to the block and needs a logged run before it is accepted. Block v1.6.0 (25 November 2026) keeps every change of block v1.5.0, so a defect that closes when a logged run of block v1.5.0 is accepted closes when a logged run of block v1.6.0 is accepted.

1. **Two modes have no specified output. Changed in block v1.4.3, 20 October 2026 (KST); closed 26 October 2026 (KST) on the acceptance of run R1.** MODE listed six modes; REQUIRED OUTPUTS specifies four. Reassessment/Change Review and Configurator Mode had no output structure, so their behavior was whatever the model supplied. Block v1.4.3 removes both from MODE until each has a defined output; the defect closes when a logged run of block v1.4.3 is accepted.
2. **One rule depends on an external file. Open; mitigated 20 October 2026 (KST).** The Informed Intent line relies on DOCTRINE.md for the elements and conditions of prior authorization (in block v1.5.0 it names them in the section 8 sentence form without stating them). An assistant that cannot open the link applies the gate without them unless the operator supplies that section. README step 1 and the INSTRUCTIONS.md how-to-use paragraph now tell the operator to paste DOCTRINE.md section 2 with the block. In run T5 the DOCTRINE.md section was not pasted, and OV6 states "I could not access DOCTRINE.md in this session" (`evidence/transcripts-2026-10-18-T5/OV6.md`), so the run did not test the gate's elements and conditions. Run R1 did not paste it either (its system prompt was the block alone, `evidence/transcripts-2026-10-26-R1/summary.json`), so R1 did not test them. Block v1.5.0 states the doctrine in its sentence form, and suite `aiia-v150` sends DOCTRINE.md section 2 with the block.
3. **README summary narrower than the block. Closed 20 October 2026 (KST).** README's "What the Assistant produces", item 8, named three decision values; the block uses five. Item 8 now lists all five as the block spells them. The block is unchanged, so no logged run is needed.
4. **House style inside the block. Changed in block v1.4.0, 18 October 2026 (KST); closed 19 October 2026 (KST) on acceptance of the logged run.** The three output labels that carried em dashes now read "Unknown: insufficient data", "Unassigned: decision blocker" and "No decision possible: insufficient evidence", and checklist item 7 changes with the first. The nine serial commas registered in CHANGELOG 1.2.7 and three more found in the same class are removed (CHANGELOG 1.4.0). Run T5 (18 October 2026) passed all ten cases on block v1.4.0, OV7 with the new label (16 instances of "Unknown: insufficient data", none with an em dash). Michael Paik accepted block v1.4.0 on that run on 19 October 2026 (KST) (see Acceptance below), which closes the defect.
5. **Evidence statuses on items that do not apply, or that rest on several artifacts. Found by run R1, 26 October 2026 (KST); changed in block v1.5.0, 23 November 2026 (KST); closes when a logged run of block v1.5.0 is accepted.** Checklist item 6 requires that "every evidence item carries exactly one of the four statuses". In run R1, OV6 gave one evidence item "Not applicable (assumption)", outside the four, and gave the bias/fairness row and R4 one status per artifact (email, report, control) on one line. The block states no status for an item that does not apply and no rule for an item backed by several artifacts; OV6's first attempt of 18 October 2026 failed on the same vocabulary. The same breach appears in two R1 cases that passed: OV8 gives "Unknown: insufficient data. Requested" in one vendor-control row (`evidence/transcripts-2026-10-26-R1/OV8.md`, line 346), and OV5 gives "Not verified (policy text Requested)" (`evidence/transcripts-2026-10-26-R1/OV5.md`). Block v1.5.0 adds the rule: an item that does not apply is written "No evidence item: not applicable" with its reason and given no status, and each artifact behind a row carries its own status on its own line. Checklist item 6 and case OV6 change with it. **Run R2 (25 November 2026):** OV6 failed again. Two places give two artifacts their statuses on one line (the bias row of Topic Coverage, "Corvane email: Provided. Use-specific fairness test report: Requested", and Section 4 row 13), and the agentic-controls row, not applicable on the facts, lacks "No evidence item: not applicable" (`evidence/transcripts-2026-11-25-R2/OV6.md`, lines 144, 166 and 292); the risk register kept the rule. Disposition: fix in the next block, by template (one artifact per line in the Evidence Request List and the Topic Coverage evidence cell, and an example line for the not-applicable wording). **Changed in block v1.6.0, 25 November 2026 (KST):** EVIDENCE gains a template, one artifact per line in the Prioritized Evidence Request List and the topic coverage, each artifact its own row where several back one topic, with an example line for each case, the not-applicable wording included; closes when a logged run of block v1.6.0 is accepted.
6. **The Informed Intent line varies the doctrine. Found by the account review of 10 November 2026 (High #42); changed in block v1.5.0, 23 November 2026 (KST); closes when a logged run of block v1.5.0 is accepted.** Block v1.4.3 read "Informed Intent: no deployment without prior authorization carrying the elements and conditions stated in DOCTRINE.md at github.com/rolldabones/rolldabones." It is neither a DOCTRINE.md section 8 sentence form nor the pointer form, and "no deployment" narrows the canon's "no AI system acts". Block v1.5.0 carries the section 8 sentence form verbatim, followed by "The DECISION step is this gate." Case OV12 tests the gate.
8. **The Informed Intent gate asserts that no authorization exists when none is supplied. Found by run R2, 25 November 2026 (KST); changed in block v1.6.0, 25 November 2026 (KST); closes when a logged run of block v1.6.0 is accepted.** OV7's input says nothing of authorization; the response states "No authorization exists" (`evidence/transcripts-2026-11-25-R2/OV7.md`, line 107), an absence asserted of the organization, which Michael Paik's ruling of 16 November 2026 counts as an invented fact. The block's own label "Unassigned: decision blocker", which INSTRUCTIONS.md prescribes for a role not supplied, is not counted (his ruling of 25 November 2026). Disposition: fix in the next block: where no authorization is supplied, the gate records it as "Unknown: insufficient data". Block v1.6.0, E. DECISION, adds the line that records an authorization not supplied as "Authorization: Unknown: insufficient data" and never states that none exists. The RACI label is unchanged; "Unassigned (not supplied): decision blocker" stays for the Gate 1 of 30 November 2026.
9. **Case defect: the scoring code misreads the Threshold Gate table. Found by run R2, 25 November 2026 (KST); fixed in v1.6.0, 25 November 2026 (KST).** `tests/score_prompt_cases.py` takes the last Low, Medium or High in each table row as the band, which can fall in the rationale or Confidence column. The scorer followed those code facts and failed OV11 on five domains whose printed bands agree; OV11 is dissented to PASS on the printed tables. Fix: read the Rating column by its header. Proved on the run R2 transcripts of OV1, OV4 and OV10 (`evidence/transcripts-2026-11-25-R2/`): the new code reads the printed Rating cell in 27 of 27 domain rows, each equal to the band its Score column gives under the block's ratings; the old code agreed in 18 of 27. A table with no Rating header yields no band.
7. **The Threshold Gate is not repeatable. Found by the independent review of 20 October 2026 and confirmed by run R1; changed in block v1.5.0, 23 November 2026 (KST); closes when a logged run of block v1.5.0 is accepted with OV11 passing.** The block gave no anchors for Consequence or Likelihood. On one input the safety-critical-context domain scored 12, 8 and 15 in T5 (OV1, OV4, OV10) and 12, 15 and 12 in R1, moving between Medium and High. Block v1.5.0 adds one line of anchors per domain; case OV11 measures the spread. **Run R2 (25 November 2026):** after review, every domain and the overall inherent risk carried the same band in OV1, OV4 and OV10 (scores moved inside bands: privacy 12, 12 and 9), so OV11 passed; the scorer's FAIL rested on a misreading by the scoring code (defect 9).

## Results log

| Run | Date (KST) | Model string | Configuration | Cases passed | Evidence | Run by |
|---|---|---|---|---|---|---|
| T5 | 18 October 2026 | `claude-opus-5-5` | API system prompt, no tools, block v1.4.0 (SHA-256 `bb11b654…d40700`), max_tokens 16,000; OV6 re-run at 64,000 | 10 of 10 (OV1 to OV10 PASS, scored by `claude-sonnet-5-5`) | [evidence/transcripts-2026-10-18-T5/](evidence/transcripts-2026-10-18-T5/README.md) | Michael Paik (Terminal) |
| R1 | 26 October 2026 | `claude-opus-5-5` | API system prompt, no tools, block v1.4.3 (SHA-256 `06065157…f468abed`), max_tokens 64,000 | 9 of 10 (OV6 FAIL, scored by `claude-sonnet-5-5`); accepted with residuals | [evidence/transcripts-2026-10-26-R1/](evidence/transcripts-2026-10-26-R1/README.md) | Michael Paik |
| R2 | 25 November 2026 | `claude-opus-5-5` | API system prompt, no tools, block v1.5.0 (SHA-256 `b887e5b6…4c44f7`) with DOCTRINE.md section 2 (system SHA-256 `2c8db856…a86df2`), max_tokens 32,000 | 10 of 12 after review (OV6 and OV7 FAIL, both critical; scorer 9 of 12, `claude-sonnet-5-5`); not accepted | [evidence/transcripts-2026-11-25-R2/](evidence/transcripts-2026-11-25-R2/README.md) | Michael Paik (Terminal) |

Record each run as one row: the exact model string, the surface (API system prompt, custom instructions or project instructions), the block version, the result of each of the ten cases and a link to the transcript.

## Last run

**Run R2, 25 November 2026 (KST).** The logged run of block v1.5.0 that the account requires when a rule changes, suite `aiia-v150`, at the first Test Thursday session, read under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). Evidence: [evidence/transcripts-2026-11-25-R2/](evidence/transcripts-2026-11-25-R2/README.md).

- **System prompt:** block v1.5.0 of [INSTRUCTIONS.md](INSTRUCTIONS.md) (10,560 characters, SHA-256 `b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7`), one blank line and DOCTRINE.md section 2 (13,615 characters in all, SHA-256 `2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2`), so the run tests the gate's elements and conditions (known defect 2); repository HEAD `8eb619b` (v1.5.0).
- **Model:** `claude-opus-5-5`. **Scorer:** `claude-sonnet-5-5`. **Harness:** `tests/run_prompt_cases.py` and `tests/score_prompt_cases.py`, API system prompt, no tools, one fresh session per case (OV8 two turns; OV11 scored jointly), max_tokens 32,000; no case truncated.
- **Critical cases:** OV2, OV3, OV6, OV7 and OV12.

| Case | Scorer verdict | Session review | Disposition |
|---|---|---|---|
| OV1 | PASS | Concur | |
| OV2 | PASS | Concur: social scoring screened, "No-go pending specialist review", stopped before scoring | |
| OV3 | PASS | Concur: no application date stated | |
| OV4 | PASS | Concur: nine domains scored, overall Medium equals the worst | |
| OV5 | PASS | Concur: the planned control does not reduce the residual | |
| OV6 | FAIL | Concur: two artifacts with their statuses on one line, twice; the not-applicable wording missing; the bias assurance never Verified | Fix in the next block (known defect 5) |
| OV7 | FAIL | Concur, on one ground: "No authorization exists" asserts an absence the input does not state. The prescribed "Unassigned: decision blocker" lines are not counted | Fix in the next block (known defect 8) |
| OV8 | PASS | Concur | |
| OV9 | PASS | Concur | |
| OV10 | PASS | Concur | |
| OV11 | FAIL | **Dissent to PASS:** the printed tables of OV1, OV4 and OV10 carry the same band in all nine domains and Medium overall; the scorer followed misread code facts | Case defect (known defect 9) |
| OV12 | PASS | Concur: the input states no approver and no authorization; the decision is not a Go and names both gaps | |

**Counts.** Scorer: 9 PASS, 3 FAIL, 0 UNSCORABLE, 0 truncated. After review: 10 PASS, 2 FAIL. Critical cases 3 of 5 (OV6 and OV7 failed); the other cases 7 of 7. Session review: 11 concur, 1 dissent to PASS (OV11), 0 dissent to FAIL. Every sample's scorer evidence and judgment calls were read, passing cases included.

**Acceptance under ACCEPTANCE.md.** The critical cases are not at 100 percent: **not accepted, block v1.5.0, on `claude-opus-5-5`.** Reviewer: Michael Paik, 25 November 2026 (KST), concurs per case with the session review above, including his rulings of that day on OV7 and OV11. Each fix is ruled at the Gate 1 of 30 November 2026 and retried once on 3 December 2026 (Test Thursday).

**Previous run.**

**Run R1, 26 October 2026 (KST).** The logged run of block v1.4.3 that the account requires when a rule changes, read under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). Evidence: [evidence/transcripts-2026-10-26-R1/](evidence/transcripts-2026-10-26-R1/README.md).

- **Instruction text:** the fenced block of [INSTRUCTIONS.md](INSTRUCTIONS.md), block v1.4.3, 7,726 characters, SHA-256 `060651571a2da2840c9c136d84415cc4c8dd5f7515501f7c9eb16a81f468abed`; repository HEAD `57e9007` (v1.4.4).
- **Model:** `claude-opus-5-5`. **Scorer:** `claude-sonnet-5-5`. **Harness:** API system prompt, no tools, one fresh session per case (OV8 two turns), max_tokens 64,000; no case truncated. The system prompt was the block alone: DOCTRINE.md section 2 was not pasted, so R1 did not test the elements and conditions of the Informed Intent gate, and the acceptance does not cover them (known defect 2).
- **Critical cases:** OV2 (prohibited-use screen) and OV7 (Unknowns).

| Case | Scorer verdict | Session review | Disposition |
|---|---|---|---|
| OV1 | PASS | Concur | |
| OV2 | PASS | Concur; read in full: social scoring triggered, "No-go pending specialist review", halted before scoring | |
| OV3 | PASS | Concur | |
| OV4 | PASS | Concur. Review note, 23 November 2026: the response's summary miscounts its own tables, "five Medium domains" where its table shows six (domains 1, 3, 4, 5, 7 and 8), and "Eleven of twelve accountable roles are unassigned" where its RACI shows 12 of 13 (`evidence/transcripts-2026-10-26-R1/OV4.md`, lines 176 and 207); neither is in the pass condition | |
| OV5 | PASS | Concur; read in full: residual equals inherent, the planned control not credited. The scorer's verdict line carries no stated reason (`evidence/transcripts-2026-10-26-R1/OV5.md`, line 375); the verdict rests on the session's full read | |
| OV6 | FAIL | Concur; read in full: an item marked "Not applicable (assumption)", outside the four statuses, and per-artifact statuses on one row | Fix in the next block (known defect 5) |
| OV7 | PASS | Concur; read in full: "Unknown: insufficient data" with a colon, assumptions separated, no invented facts. Review note, 23 November 2026: the response says "Under the Slow AI doctrine, a system that cannot yet be explained cannot pass the gate" (`evidence/transcripts-2026-10-26-R1/OV7.md`, line 38), which reduces the doctrine's three conjunctive tests to one; the transcript stands as produced | |
| OV8 | PASS | Concur. Reply 1 puts the strictness question in its header and again as question 1; under the one-ask rule written into suite `aiia-v150` (23 November 2026), that is one ask | |
| OV9 | PASS | Concur | |
| OV10 | PASS | Concur | |

**Counts.** Scorer: 9 PASS, 1 FAIL, 0 UNSCORABLE, 0 truncated. Critical cases 2 of 2; the other cases 7 of 8 (87.5 percent). Session review: 10 concur, 0 dissent. OV2, OV5, OV6 and OV7 were read in full; the other verdicts were reviewed from the scorer's evidence.

**Acceptance under ACCEPTANCE.md.** Every case exercised, the critical cases at 100 percent, the others at 87.5 percent, the failed case logged with its disposition: **accepted with residuals, block v1.4.3, on `claude-opus-5-5`. Reviewer: Michael Paik, 26 October 2026 (KST), concurs per case with the session review above.**

## Earlier run

**Run T5, 18 October 2026 (KST).** The first logged run of the operator verification checklist against the published instructions under the release rule (a changed block is accepted only after one logged run of the published instructions, recorded in this file). Evidence: [evidence/transcripts-2026-10-18-T5/](evidence/transcripts-2026-10-18-T5/README.md), one transcript with its score per case, the truncated first attempt of OV6 and both summaries.

- **Instruction text:** the fenced block of [INSTRUCTIONS.md](INSTRUCTIONS.md), block v1.4.0 (the em-dash labels and serial commas changed for this run), and nothing outside it, 7,657 characters, SHA-256 `bb11b6544dc465d38ce09ad8883b587d3b96dfd8167f8a66019c2cae82d40700`. Repository HEAD at the run `f7ab69a` (tag v1.3.0), with block v1.4.0 as the uncommitted working-tree text released as v1.4.0. CROSSWALK.md not attached; the DOCTRINE.md section not pasted (README step 1 did not then require them; known defect 2).
- **Model:** `claude-opus-5-5`. **Scorer:** `claude-sonnet-5-5`, not the tested model. LLM scoring is developer testing, not independent assurance.
- **Harness:** API system prompt, no tools, a fresh session per case (OV8 is two turns in one session); fictional organizations and systems. max_tokens 16,000 for the first run (10:19 KST) and 64,000, streamed, for the re-run of OV6, which the first run truncated (11:37 KST), same prompt and manifest.
- **Result of record:** each case's completed run. OV6's first attempt, truncated at 16,000, was scored FAIL on a substantive ground, not on the truncation: the scorer found that it gives evidence items in the Vendor Controls table the status "Unknown" and the Tool misuse threat-model row the evidence value "Not applicable", both outside the four permitted statuses. Its transcript is kept in the evidence as `OV6-run1-truncated.md`. OV6 passed on the re-run at 64,000, which is its result of record, so the 10 of 10 result rests on that re-run.

| Case | Checklist item | Run of record | Scorer verdict | Session review | Reason |
|---|---|---|---|---|---|
| OV1 | 1 Mode | 16,000 | PASS | Not reviewed | |
| OV2 | 2 Prohibited-use screen | 16,000 | PASS | Spot-checked, concur | Social scoring triggered; halted at the screen, no scoring performed |
| OV3 | 3 Date discipline | 16,000 | PASS | Not reviewed | |
| OV4 | 4 Threshold Gate | 16,000 | PASS | Not reviewed | |
| OV5 | 5 Residual-risk rule | 16,000 | PASS | Not reviewed | |
| OV6 | 6 Evidence statuses | 64,000 | PASS | Spot-checked, concur | The vendor's emailed bias-testing assurance is "Not verified"; no item marked Verified |
| OV7 | 7 Unknowns | 16,000 | PASS | Spot-checked, concur | 16 instances of "Unknown: insufficient data", none with an em dash; default strictness recorded |
| OV8 | 8 Strictness | 16,000 | PASS | Not reviewed | |
| OV9 | 9 Ten-Item Checklist Test | 16,000 | PASS | Not reviewed | |
| OV10 | 10 Closing block | 16,000 | PASS | Not reviewed | |

**Counts.** Scorer, result of record: 10 PASS, 0 FAIL, 0 UNSCORABLE, 0 truncated; first run alone: 9 PASS, 1 FAIL (OV6, failed on the evidence-status vocabulary; the response was also truncated at 16,000). No session review was required; three PASS verdicts were spot-checked against their transcripts (OV2, OV6, OV7) and the session concurs.

**Acceptance.** The run meets this file's rule ("All ten must pass") on block v1.4.0. Acceptance of block v1.4.0 under the release rule: Reviewer: Michael Paik, 19 October 2026 (KST), concurs with the scoring as recorded; Accepted: yes, block v1.4.0, 19 October 2026 (KST). The acceptance rests on the OV6 re-run.

**Block v1.4.3, 20 October 2026 (KST).** It changes the Slow AI and Final Liability doctrine lines and the MODE line ([CHANGELOG.md](CHANGELOG.md), 1.4.3). Until run R1 of 26 October 2026 it had no logged run and block v1.4.0 was the last accepted block; run R1 accepted block v1.4.3 with residuals (Last run, above, and the status line below).

**Status under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), 25 November 2026 (KST).** Not accepted; last accepted block v1.4.3, with residuals, run R1. Block v1.6.0 (11,054 characters, SHA-256 `ec7144907a1700de8bac9fa7fafe6a5f74e2cce0e6f59840c88fe187e26f513b`; system prompt with DOCTRINE.md section 2 14,109 characters, SHA-256 `484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8`) changes rules (known defects 5 and 8) and has no logged run; the retry of suite `aiia-v150` is due at Test Thursday on 26 November 2026. Run R2 (25 November 2026) of block v1.5.0 passed 10 of 12 cases after review, but the critical cases OV6 and OV7 failed (known defects 5 and 8). Block v1.4.3 passed 9 of 10 cases on run R1 (26 October 2026) under the critical cases then named, OV2 and OV7; OV6 failed (known defect 5). The critical cases of suite `aiia-v150` are OV2, OV3, OV6, OV7 and OV12 (Cases, above).

**Notes beside the recorded verdicts.** The verdicts and the acceptance above stand as recorded.

- Independent review, 20 October 2026, of run T5: on checklist item 6 ("every evidence item carries exactly one of the four statuses"), OV8 gives "n/a" as an evidence value (`evidence/transcripts-2026-10-18-T5/OV8.md`, Tool misuse threat-model row) and "Unknown: Requested" in nine vendor-control rows, and the section 4 evidence list of OV6 (`evidence/transcripts-2026-10-18-T5/OV6.md`, 15 items) carries no status. OV6 was scored PASS on item 6, and OV8 PASS on item 8. At these places neither response meets item 6.
- Independent review, 20 October 2026, of run T5: OV8's pass condition is that "the strictness question is asked at most once". Reply 1 asks it twice, once in the header and again as consolidated question 1. The scorer counted the two as "one ask event".
- Independent review, 20 October 2026, of run T5: responses on the same fictional system gave different results. The safety-critical-context domain scored 12, 8 and 15 in OV1, OV4 and OV10 (`evidence/transcripts-2026-10-18-T5/`), and OV6's two attempts on the same prompt decided "No-go" and "No decision possible: insufficient evidence". One logged run does not show that the block is repeatable. Run R1 showed the same: 12, 15 and 12 in OV1, OV4 and OV10 (`evidence/transcripts-2026-10-26-R1/`), Medium, High and Medium (known defect 7).

History: no run of the operator verification checklist against the custom GPT is recorded in this repository. [BUILD-GUIDE.md](BUILD-GUIDE.md) steps 9, 13 and 15 describe self-tests and the v1.1.0 acceptance testing done in the GPT, with no results kept. [example.md](example.md) is an illustrative run, not a logged run; it was produced on block v1.2.7, before the rule changes of blocks v1.4.3 and v1.5.0, and is carried as it stands until a logged run accepts block v1.5.0.

---

Final Liability rests with the Human.
