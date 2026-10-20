# CHANGELOG.md

All notable changes to this repository. Versions follow semantic versioning. Prior versions are superseded upon release of the next.

Maintenance note (2026-07-14): a stale draft block duplicating the [1.2.1] entry and carrying an inaccurate [1.2.0] writeup (it described a SPEC.md that was never shipped) was removed from the top of this file. The retained [1.2.0] entry reflects the files actually released.

## [1.4.3] - 2026-10-20

Patch. Independent review of 20 October 2026; changes made with Claude, approved by Michael Paik. Findings applied: AIA-01, AIA-02, AIA-03, AIA-04, AIA-05, AIA-06, AIA-07, AIA-08, AIA-09, AIA-10, AIA-11, AIA-12, AIA-13, AIA-14, AIA-15, AIA-17, AIA-18, AIA-19, AIA-21, AIA-22, AIA-23, AIA-25, X-01, X-02. No change for AIA-16 (disclosure at tests.md stands) and AIA-20 and AIA-24 (owner-accepted).

- **Instruction block v1.4.0 to v1.4.3 (AIA-06, X-01). Not accepted pending a logged run;** block v1.4.0 stays the last accepted block. The block measures 7,726 characters, SHA-256 `060651571a2da2840c9c136d84415cc4c8dd5f7515501f7c9eb16a81f468abed` (UTF-8 text between the fences, without the final newline), against 7,657 and `bb11b654…d40700` at v1.4.0.
  - Old: `* Slow AI: evidence over assurances; governed, explainable, auditable, reversible.` New: `* Slow AI: AI that cannot be governed, explained and audited is not deployed; the three tests are conjunctive, and the doctrine is a precondition, not a speed limit.` (DOCTRINE.md section 8 sentence form, verbatim.)
  - Old: `* Final Liability: every material risk, control, exception, escalation, decision and kill-switch has a named human owner.` New: `* Final Liability rests with the Human: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene.` (DOCTRINE.md section 8 sentence form, verbatim.)
  - Old: `... Full Assessment; Reassessment/Change Review; or Configurator Mode.` New: `... Preliminary Intake; or Full Assessment.` The two modes had no defined output (tests.md known defect 1).
- **`INSTRUCTIONS.md`:** header to block v1.4.3 with "not accepted pending a logged run"; the character count; the how-to-use paragraph tells the operator to paste DOCTRINE.md section 2 with the block (AIA-07); a glossary line for CSAM outside the fence (AIA-23); a "What changed in v1.4.3" section; checklist item 1 reads "from the four defined"; "ruling 9" replaced by a plain statement of the release rule (AIA-11); closing status line.
- **Test record (`tests.md`, evidence README):** OV6's first attempt is recorded as a substantive FAIL on the evidence-status vocabulary, not a non-event, and the acceptance of block v1.4.0 is stated to rest on the re-run (AIA-01). Dated independent-review notes are added beside the recorded verdicts for OV8 and OV6 on checklist item 6 (AIA-12), OV8's two strictness asks in reply 1 (AIA-15) and the run-to-run variation (AIA-14); the recorded verdicts and acceptance stand. Known defects 3 and 4 are marked closed (AIA-02, AIA-03), defect 1 changed pending a logged run and defect 2 mitigated. The evidence README states that the scoring rubric is not shipped and that the verdicts cannot be reproduced from the repository (AIA-10). Internal labels ("ruling 9", "session T5 Block A") are replaced by plain statements (AIA-11).
- **Accuracy:** the Article 50(2) transition is cited to Article 111(4) of Regulation (EU) 2024/1689, inserted by Regulation (EU) 2026/1744, Article 1, point (39)(b), with Recital 38 as context, in `README.md` and `CROSSWALK.md` (AIA-05); the Official Journal date of Regulation (EU) 2024/1689 is 12 July 2024 (AIA-17); `CROSSWALK.md` no longer calls the paragraph-number form of the Article 113 pinpoint incorrect, since the Regulation itself uses it in Article 111(1); the house form stays "Article 113, third paragraph" (X-02); `example.md` records that its output mislabels eight RACI owners and three register owners and miscounts them, with the output left as produced (AIA-09).
- **Consistency and usefulness:** README "What the Assistant produces" item 8 lists all five decision values (AIA-03); `CROSSWALK.md` status line, which lagged at v1.2.5, is in step with its masthead (AIA-04) and its currency-note heading records the amendments (AIA-18); `BUILD-GUIDE.md` no longer says Phases 1, 2 and 5 stand as written on any platform (AIA-13); adopters are told to keep their own run log (AIA-25); the README doctrine sentence uses the DOCTRINE.md pointer and sentence forms (X-01); the README states that one logged run does not show repeatability (AIA-14) and how to ask for commercial use permission (AIA-08); the "Nearest neighbors" lead-in introduces its list (AIA-22); KST, SLIs/SLOs, RACI and GPAI are spelled out at first use (AIA-23).
- **Errata to shipped entries (entries below are left as cut):** the [1.2.0] entry renders the gap label as "Unassigned: decision blocker", but v1.2.0 shipped the em-dash form "Unassigned—decision blocker", which block v1.4.0 changed (AIA-19). Versions 1.0.0, 1.1.0 and 1.2.0 were not tagged; tags start at v1.2.1 (AIA-21).
- **Versions:** Version line, How to Cite, Status line and `CITATION.cff` to v1.4.3 in lockstep; `INSTRUCTIONS.md`, `tests.md` and `BUILD-GUIDE.md` mastheads to v1.4.3; `CROSSWALK.md` to its own v1.2.8.

## [1.4.2] - 2026-10-20

- LICENSE: two defects against the Creative Commons legal code corrected (the space in 'ShareAlike. In'; the CC0 sentence of the closing notice). Operative terms unchanged.
- Version line, How to Cite, Status line and `CITATION.cff` to v1.4.2 in lockstep. `INSTRUCTIONS.md` is unchanged and keeps block v1.4.0.

## [1.4.1] - 2026-10-19

Patch, from the weekly maintenance sweep of 19 October 2026 (KST) and Michael Paik's review of the T5 runs, completed 19 October 2026 (KST), on which he concurs with the scoring as recorded. The weekly sweep raised A1 HIGH at `README.md:62` ("acceptance is pending review", true when written on 18 October 2026). No change to the instruction block or any rule.

- **Block v1.4.0 accepted under ruling 9.** The T5 run passed all ten operator verification checklist items; the named reviewer concurs and accepts the block. `tests.md` Acceptance line and the README Change control sentence record the review and the acceptance.
- Version line, How to Cite, Status line and `CITATION.cff` to v1.4.1 in lockstep. `tests.md` masthead to v1.4.1. `INSTRUCTIONS.md` is unchanged and keeps block v1.4.0.

## [1.4.0] - 2026-10-18

Minor release, session T5 of the whole-account review of 15 October 2026 (KST), review doc section 5 (untested instruments) and the T5 row of the session plan: the ruling 9 logged run of the block T4 re-statused, with the block's em-dash labels and serial commas changed in the same run. Amendment note, 18 October 2026 (KST): the instruction block changes from v1.2.7 to v1.4.0 for house style only; no rule, mode, threshold, status value or output section is added, removed or reordered. The change is made so that the first logged run tests the changed text; it is accepted only when that run passes and is recorded in `tests.md` (ruling 9). No legal or regulatory statement changed.

- **Instruction block, three output labels (tests.md known defect 4).** Each em dash becomes a colon and a space. These are labels the Assistant writes into its output, so outputs change with them.
  - Old: `Label missing facts “Unknown—insufficient data,”` New: `Label missing facts “Unknown: insufficient data,”`
  - Old: `No decision possible—insufficient evidence.` New: `No decision possible: insufficient evidence.`
  - Old: `If absent, use “Unassigned—decision blocker.”` New: `If absent, use “Unassigned: decision blocker.”`
- **Instruction block, the nine serial commas registered in 1.2.7 (tests.md known defect 4).** Each comma before the final "and" or "or" is removed; nothing else in the line changes.
  - Old: `NIST AI RMF, ISO/IEC 42001, and ISO/IEC 42005.` New: `NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005.`
  - Old: `escalation, decision, and kill-switch has a named human owner.` New: `escalation, decision and kill-switch has a named human owner.`
  - Old: `approval checkpoints, interruption, and rollback.` New: `approval checkpoints, interruption and rollback.`
  - Old: `malicious outputs, and logging integrity.` New: `malicious outputs and logging integrity.`
  - Old: `incident duties, termination, and deletion.` New: `incident duties, termination and deletion.`
  - Old: `tested rollback/kill switch, and revalidation triggers.` New: `tested rollback/kill switch and revalidation triggers.`
  - Old: `inaccessible, outdated, or unsupported` New: `inaccessible, outdated or unsupported`
  - Old: `approvals, and change records.` New: `approvals and change records.`
  - Old: `law enforcement, or essential services` New: `law enforcement or essential services`
- **Instruction block, three further serial commas of the same class, found in this release and not in the 1.2.7 register.** Removed with the nine.
  - Old: `name the escalation path and evidence required, and stop before scoring.` New: `name the escalation path and evidence required and stop before scoring.`
  - Old: `state assumptions and confidence (Low/Medium/High), and name evidence` New: `state assumptions and confidence (Low/Medium/High) and name evidence`
  - Old: `Status: [↻ v1], [⇥ pending], or [✓ locked]` New: `Status: [↻ v1], [⇥ pending] or [✓ locked]`
- **Not changed in the block:** the semicolon-separated lists ending "; or" (the MODE line and the prohibited-use screen), which are not serial commas; the en dashes in the score ranges.
- **Measurement.** The block measures 7,657 characters (UTF-16 code units, which here equal code points), SHA-256 `bb11b6544dc465d38ce09ad8883b587d3b96dfd8167f8a66019c2cae82d40700` (UTF-8 text between the fences, without the final newline), against 7,666 and `d5f310e64a328422ef85bfd2bed036f3a3072c8fa086981dcdc2d1b9dafdb604` at v1.2.7: twelve commas out, three colon-spaces in for three em dashes. Under the 8,000-character builder ceiling `BUILD-GUIDE.md` step 6 reports, which no longer binds.
- **`INSTRUCTIONS.md`:** header to `block v1.4.0`; the last-verified sentence names the v1.4.0 changes and that the GPT never carried them; the how-to-use count to 7,657; a "What changed in v1.4.0" section; the v1.2.7 history sentence reads "At v1.2.7 the block measured 7,666 characters"; operator verification checklist item 7 tests "Unknown: insufficient data", changed with the label it tests; closing status line `v1.4.0 (block v1.4.0)`.
- **Run T5, 18 October 2026 (KST):** suite `aiia`, the ten operator verification checklist items as OV1 to OV10, tested model `claude-opus-5-5`, scored by `claude-sonnet-5-5` (LLM scoring, developer testing, not independent assurance), API system prompt with block v1.4.0 only, no tools, fictional inputs. First run at max_tokens 16,000: 9 PASS, OV6 truncated; OV6 re-run at max_tokens 64,000, streamed, same prompt and manifest: PASS. **Result of record: 10 of 10 PASS.** No FAIL, so no session review was required; three PASS verdicts spot-checked (OV2, OV6, OV7): concur. OV7 shows the changed label in use (16 instances of "Unknown: insufficient data", none with an em dash). The run meets the rule "All ten must pass"; acceptance of block v1.4.0 under ruling 9 is pending review (Reviewer: pending (Michael Paik)).
- **`tests.md`:** known defect 4 marked changed in block v1.4.0 and passing in run T5, closing on acceptance; the Results log carries the T5 row; Last run rewritten as the run record (configuration with both max_tokens values, per-case table, counts, acceptance); version line to v1.4.0.
- **`evidence/transcripts-2026-10-18-T5/` (new):** the ten transcripts of record, OV6's truncated first attempt as `OV6-run1-truncated.md`, both summaries and a `README.md` index. Transcripts are copied byte for byte with only the closing line appended; model output is verbatim and not edited.
- **`example.md`:** one sentence added under the header saying the output is left as produced on block v1.2.7, so its labels carry that block's em-dash form. The output is not edited: it is what the run produced.
- **`README.md`:** masthead, the Run it in three steps count (7,666 to 7,657), How to Cite and the status line to v1.4.0; Change control states the run's result. **`CITATION.cff`:** `version` 1.4.0, `date-released` 2026-10-18. In lockstep with this entry; the tag is v1.4.0.
- **Findings by class (review doc section 5; tests.md known defect 4):** confirmed and edited, the three em-dash labels and nine registered serial commas; found in class and edited, three further serial commas; already fixed, none; not reproducible, none.
- **Deferred, with reasons:** known defects 1 to 3 (two modes without output, the DOCTRINE.md dependency, the README decision values) are not house style and stay recorded for a later changed block; `CROSSWALK.md` and `BUILD-GUIDE.md` are unchanged and keep their own version lines.
- Shipped entries below are left as written (ruling 7 of 15 October 2026).

## [1.3.0] - 2026-10-18

Minor release, session T4 of the whole-account review of 15 October 2026 (KST), review doc section 4 (the custom-GPT retirement cliff) and reviewer report 12 items A1, A2, A12, A18, B4, B5, B9 and C5, under determination D5 and ruling 9. The custom GPT was retired on 1 October 2026 and converted to a private plug-in on the OpenAI platform; its configuration is Locked as of that date. Block v1.2.7 in `INSTRUCTIONS.md` becomes the instrument of this repository and the text of record; block v1.2.1, the text last verified against the GPT, is archived below. No legal or regulatory statement changed: `CROSSWALK.md` and the README's amendment notes are untouched.

- **`INSTRUCTIONS.md` (A1):** the header is rewritten as an instrument status line (`Instrument · block v1.2.7 · 18 October 2026 (KST) · text of record`), the retirement sentence, the last-verified sentence and a how-to-use paragraph; the heading "The deployed instruction block" reads "The instruction block"; a "What changed in v1.3.0" section is added; the checklist preamble asks for each run to be recorded in `tests.md`; the closing status line reads `v1.3.0 (block v1.2.7)`. The superseded header sentences are struck below. The v1.2.7 history paragraph that linked `INSTRUCTIONS-EXTENDED.md` now names it as removed and recoverable at tag v1.2.12.
- **The instruction block itself is unchanged.** It was checked for every GPT-only dependency: Code Interpreter or any other capability toggle, knowledge-file references, conversation starters and the builder's character limit. **None was found, so no wording in the block changed.** It measures 7,666 characters, SHA-256 `d5f310e64a328422ef85bfd2bed036f3a3072c8fa086981dcdc2d1b9dafdb604` (UTF-8 text between the fences, without the final newline). One external dependency remains and is recorded as a known defect in `tests.md`: the Informed Intent line points to DOCTRINE.md, which an assistant without link access cannot open; the how-to-use paragraph tells the operator to paste that section alongside.
- **Wording changes from the last verified text (v1.2.1) to the instrument (v1.2.7):** one line, made in 1.2.7 and never carried by the GPT.
  - Old: `* Informed Intent: no production deployment without pre-authorization covering purpose, scope, limits, owner, and approver.`
  - New: `* Informed Intent: no deployment without prior authorization carrying the elements and conditions stated in DOCTRINE.md at github.com/rolldabones/rolldabones. The DECISION step is this gate.`
- **`README.md`:** masthead in the instrument form; the retirement notice replaced by the standard one-line retirement statement linking the account's RETIREMENT.md; the opening paragraph becomes **What it does**, recast from "a custom GPT (or equivalent on any capable AI platform)" to an instruction block for any current assistant; Quickstart becomes **Run it in three steps**; the 8,000-character builder limit is no longer stated as fact (A18; the count of 7,666 was already corrected in 1.2.12, A2 already fixed); the reference implementation line is removed, its model recorded as history under **Change control**, a new section; the Files table adds `tests.md`, `example.md` and `CITATION.cff` (B9) and describes `INSTRUCTIONS.md` as the instrument. How to Cite and the status line to v1.3.0.
- **`INSTRUCTIONS-EXTENDED.md` removed (A12, B4).** It was the v1.1.0 long form, lacking five rules the block carries (the residual-risk evidence rule, the five-value decision taxonomy, mode declaration, default strictness and the self-check), and closed by calling itself a "reference companion to v1.2.0", the open question 1.2.8 left undecided. A reader following it had to hand-port five rules. It is deleted rather than regenerated; it is recoverable at tag v1.2.12. Every reference to it is removed from live text.
- **`BUILD-GUIDE.md` to v1.3.0 (B5):** an amendment note under the introduction; Phases 3 and 4 headed and marked as the historical GPT build; a new **Build it now** section maps steps 7 to 10 and 13 to a system prompt, an optional `CROSSWALK.md` reference, the operator verification checklist and a logged run in `tests.md`; step 7's long-form pointer and step 15's "shipped as v1.2.0 (INSTRUCTIONS-EXTENDED.md and INSTRUCTIONS.md)" corrected to "shipped as v1.2.0 in INSTRUCTIONS.md only"; step 14's link struck; the builder limit in step 6 restated as reported and not found in official documentation (A18). The closing status line read v1.2.3 against a masthead of v1.2.4 after 1.2.12; both now read v1.3.0.
- **`tests.md` added:** points to the [Operator verification checklist](INSTRUCTIONS.md#operator-verification-checklist) as the case list, records four known defects, carries an empty results log and the **Last run** statement. No run is claimed.
- **`example.md` added:** one illustrative Full Assessment of a fictional bank's CV-screening assistant, labeled as not a logged run under ruling 9.
- **`CITATION.cff`:** `version` 1.3.0 and `date-released` 2026-10-18; abstract unchanged. README masthead, How to Cite, status lines, `CITATION.cff` and this entry in lockstep; the tag is v1.3.0.
- Shipped entries below are left as written (ruling 7 of 15 October 2026). `LICENSE.md` contains no sentence describing the GPT and is unchanged.

### Configuration as last deployed, Locked 1 October 2026

- **Name:** AI Impact Assessment Assistant.
- **Description:** "Produces professional, audit-ready AI impact assessments that are jurisdiction-agnostic and aligned to the EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005.", as given in `BUILD-GUIDE.md` step 8 as the example used. Whether it is the exact deployed text: Unknown.
- **Conversation starters:** Unknown (not recorded in this repository).
- **Capabilities:** Code Interpreter on (`BUILD-GUIDE.md` step 8). Web search, canvas and image generation: Unknown (not recorded).
- **Knowledge files:** none recorded in this repository. Unknown whether any were attached.
- **Actions:** none recorded.
- **Model as recorded:** GPT-5.2 Thinking, as stated in the repository. The plug-in's model: Unknown.
- **Instructions:** block v1.2.1, last verified against the GPT on 13 July 2026. The 1.2.7 correction was never deployed.
- **Public link, STRUCK 18 October 2026 (KST):** ~~https://chatgpt.com/g/g-69882df5cb388191952447d6324de455-ai-impact-assessment-assistant~~ **STRUCK.**
- **Retired** 1 October 2026 and converted to a private plug-in on the OpenAI platform.

### Last deployed instruction block, v1.2.1, last verified 13 July 2026, Locked 1 October 2026

Extracted with `git show v1.2.1:INSTRUCTIONS.md` and reproduced verbatim, including the serial commas and em dashes it shipped with. 7,599 characters (UTF-16 code units, which here equal code points), SHA-256 `93575a8ed000df959022e39c31d3a9790c3837f6aab92daaea6b784786bae5e6` (UTF-8 text between the fences, without the final newline).

```
You are “AI Impact Assessment Assistant” for enterprise use. Produce audit-ready AI impact assessments aligned with the EU AI Act risk-based approach, NIST AI RMF, ISO/IEC 42001, and ISO/IEC 42005. You are not legal counsel or the final approver. Never state regulatory dates or article-level duties from memory; require current verification with counsel or official sources. Final Liability rests with the Human.

CORE DOCTRINES

* Slow AI: evidence over assurances; governed, explainable, auditable, reversible.
* Informed Intent: no production deployment without pre-authorization covering purpose, scope, limits, owner, and approver.
* Final Liability: every material risk, control, exception, escalation, decision, and kill-switch has a named human owner.

MODE
State one mode: Instruction-Conformance Test; Ten-Item Checklist Test; Preliminary Intake; Full Assessment; Reassessment/Change Review; or Configurator Mode.

STRICTNESS
Ask once: “risk-averse enterprise” or “move fast with guardrails.” If unanswered, default to risk-averse enterprise and record it.

PROHIBITED-USE SCREEN FIRST
Before scoring, screen for harmful manipulation; exploitation of vulnerability; social scoring; sensitive-trait inference; prohibited biometric uses; non-consensual intimate imagery; CSAM; or clearly unlawful use. If triggered or unresolved, output “No-go pending specialist review,” name the escalation path and evidence required, and stop before scoring.

MISSING FACTS
Ask no more than 15 consolidated questions. Label missing facts “Unknown—insufficient data,” state assumptions and confidence (Low/Medium/High), and name evidence that would change the result. Never convert assumptions into facts. Proceed with available information when requested.

A. FRAME (MAP)
Capture: purpose/problem; users; affected stakeholders; decision domain; automation level; workflow and AI influence points; inputs/outputs/channels; scope/regions; third parties; data categories/sources; personal/sensitive data; lawful-basis or consent approach; retention/deletion; access controls; model type/source; post-deploy learning; integrations; monitoring status.

B. SYSTEM BOUNDARY
Give a short data-flow narrative: inputs/source; processing locations; third-party/cross-border transfers; outputs; storage/retention; access paths; integrations/tools; logging/audit points.

C. THRESHOLD GATE
Score Consequence 1–5 × Likelihood 1–5 for:

1. harm to people
2. rights impacts
3. discrimination
4. privacy
5. security
6. safety-critical context
7. scale/vulnerability
8. irreversibility
9. autonomy/agentic action
   Ratings: 1–6 Low, 8–12 Medium, 15–25 High. Overall inherent risk = worst domain. Any Medium or High triggers Full Assessment.

D. FULL ASSESSMENT (MEASURE/MANAGE)
For each material risk provide: statement; stakeholders; inherent score; controls; evidence status; tests/metrics; owner; due date; residual score; status.
Do not reduce residual risk because a control is planned. Planned = residual remains inherent unless justified. Implemented but unverified supports only a low-confidence estimate. Verified controls may reduce residual risk with evidence.

Cover: data provenance/quality; representativeness; bias/fairness; performance/limitations; hallucination/grounding for generative AI; robustness/adversarial testing; drift; privacy; security; human oversight; fallback/rollback/kill switch; transparency; explanation; contestability/appeal/redress; incidents; audit logs; documentation/versioning; vendor/supply chain; misuse; IP/content rights; cross-border data; change control; periodic review; decommissioning.
For agentic systems add least privilege, scoped tools, transaction limits, segregation of duties, step-level logs, approval checkpoints, interruption, and rollback.

SECURITY MINI THREAT MODEL
Include abuse cases, prompt injection/tool misuse, data exfiltration, model extraction, privilege escalation, malicious outputs, and logging integrity.

VENDOR CONTROLS
Review data use, training rights, IP/indemnities, subprocessors, change notices, audit rights, SLAs, incident duties, termination, and deletion.

E. DECISION (INFORMED INTENT GATE)
Use exactly one: Go; Go with conditions; No-go; No-go pending specialist review; No decision possible—insufficient evidence.
Go requires minimum evidence verified, no unresolved High residual risk, named owners/approver, recorded risk acceptance, operational monitoring, tested incident response, tested rollback/kill switch, and revalidation triggers.
Separate conditions precedent from conditions subsequent.

TEN-ITEM ACCEPTANCE CHECKLIST
When requested, rate each Pass/Partial/Fail/Not testable/Not applicable:

1. Permissible use
2. Informed intent
3. Accountability/RACI
4. System boundary
5. Data governance and rights
6. Model performance and fairness
7. Security and misuse resistance
8. Human oversight and stakeholder protections
9. Monitoring and lifecycle management
10. Evidence and decision authorization
    For each give rationale and evidence status. If no real system/evidence is supplied, conclude: “Process test completed; no system acceptance decision is possible.”

EVIDENCE
Use exactly one status:

* Requested: asked for, not supplied
* Provided: supplied/referenced, not reviewed
* Verified: reviewed and supports the conclusion
* Not verified: missing, inadequate, inaccessible, outdated, or unsupported
  Never mark Verified from assurance alone. Link controls to artifacts such as architecture, data flow, model/data docs, privacy/security reviews, tests, logs, policies, vendor terms, incident exercises, approvals, and change records.

RACI
Capture: business, system, model, data, risk, privacy, security, human-oversight, incident/on-call owners; kill-switch authority; deployment approver; periodic-review approver. If absent, use “Unassigned—decision blocker.”

REQUIRED OUTPUTS
Instruction-Conformance Test: requirement; result; observation; gaps; corrected behavior; overall conclusion.

Checklist Test: ten results; assumptions; confidence; evidence gaps; whether a real acceptance decision is possible.

Preliminary Intake: A. FRAME; B. SYSTEM BOUNDARY; prohibited-use result; C. THRESHOLD GATE; priority evidence; provisional decision; next step.

Full Assessment:

1. Executive Summary (10 bullets max)
2. Completed Assessment
3. Risk Register: Risk | Inherent | Controls | Evidence | Residual | Owner | Status
4. Prioritized Evidence Request List, including minimum evidence for Go
5. Test Plan: fairness, performance, robustness, privacy, security, monitoring thresholds
6. Transparency/Contestability Pack: notice, explanation template, appeal steps
7. Monitoring/Continuous Improvement: SLIs/SLOs, thresholds, cadence, drift, incidents, escalation, change control, review, decommission
8. Decision Record: classification, assumptions, confidence, sign-offs, conditions, revalidation triggers

HIGH-RISK-LIKE USES
For employment, credit, education, healthcare, critical infrastructure, biometrics, law enforcement, or essential services, require stronger controls and counsel review of possible duties. No legal advice.

SELF-CHECK
Verify: correct mode; prohibited-use screen first where applicable; assumptions separate from facts; inherent/residual risk separate; evidence not overstated; RACI included; required outputs present; decision matches evidence; legal triggers referred to counsel.

END EVERY SUBSTANTIVE RESPONSE WITH
Status: [↻ v1], [⇥ pending], or [✓ locked]
Open items: unresolved facts, evidence, risks, owners
Next step: one concrete action
Final Liability rests with the Human.
```

### Struck text, quoted

The retirement notice, `README.md`, struck as a whole on 18 October 2026 (KST) and quoted verbatim with its own earlier strike. **STRUCK 18 October 2026 (KST).**

> <del>**Retirement notice, 28 September 2026 (KST), corrected 5 October 2026 (KST).** OpenAI is retiring custom GPTs. Its [Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq), read on 28 September 2026, states that custom GPTs and their GPT pages become inaccessible on **11 December 2026**, or 11 February 2027 for Enterprise workspaces with an approved deferral. ~~The reference implementation will be retired on that date and will not be migrated.~~ **STRUCK 5 October 2026 (KST):** the reference implementation was converted to a ChatGPT plugin on 1 October 2026, and the plugin is private and not publicly listed. The same FAQ, read again on 5 October 2026, states that a migrated GPT stays usable until retirement but becomes read-only. The link above was verified resolving on 5 October 2026 and stops working on 11 December 2026.</del>
>
> <del>Everything needed to build your own stays published here: the instruction block and the configuration, including any knowledge files. OpenAI's replacement is the ChatGPT plugin, in which a GPT's instructions become a Skill and its knowledge files become reference files. Its [Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex) article, read the same day, offers plugin creation in supported ChatGPT Business and Enterprise workspaces, so check what your plan allows. The instruction block is not tied to ChatGPT and also serves as the custom instructions of any assistant that accepts them. A plugin does not inherit a GPT's selected model and custom actions do not transfer, so choose the model yourself and test before you rely on the output.</del>

- ~~Reference implementation: [AI Impact Assessment Assistant on ChatGPT](https://chatgpt.com/g/g-69882df5cb388191952447d6324de455-ai-impact-assessment-assistant) (built on GPT-5.2 Thinking; the instruction block is platform-agnostic).~~ **STRUCK 18 October 2026 (KST).** `README.md` reference implementation line. Model kept as history under Change control.
- ~~1. Copy the instruction block from [INSTRUCTIONS.md](INSTRUCTIONS.md) into your platform's system prompt or Instructions field (7,666 characters; fits the 8,000-character limit in OpenAI's GPT builder).~~ **STRUCK 18 October 2026 (KST).** `README.md` Quickstart step 1: the builder limit stated as fact (A18).
- ~~2. Name it, describe it, enable your platform's code execution feature and select a reasoning-capable model.~~ **STRUCK 18 October 2026 (KST).** `README.md` Quickstart step 2: platform configuration steps; the block needs none.
- ~~"a custom GPT (or equivalent on any capable AI platform)"~~ **STRUCK 18 October 2026 (KST).** `README.md` opening paragraph.
- `INSTRUCTIONS.md` line 3: ~~"**AI Impact Assessment Assistant · Deployed instruction block v1.2.7 · 8 September 2026**"~~ **STRUCK 18 October 2026 (KST).** The block was never deployed.
- `INSTRUCTIONS.md` line 5, quoted verbatim with its own earlier strike: <del>This is the canonical instruction block: [AI Impact Assessment Assistant on ChatGPT](https://chatgpt.com/g/g-69882df5cb388191952447d6324de455-ai-impact-assessment-assistant). ~~It is verbatim as deployed in the reference implementation.~~ **STRUCK 8 September 2026**, in this release: the Informed Intent line below was corrected to point at [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), and the deployed implementation has not yet been updated to match. **This file governs; the deployment lags it until the live GPT is updated.** It is 7,666 characters, compressed to fit the GPT builder Instructions box. If your platform accepts longer system prompts, consider [INSTRUCTIONS-EXTENDED.md](INSTRUCTIONS-EXTENDED.md), the uncompressed long form. The two are functionally aligned; where they differ, this block governs and adds the residual-risk evidence rule, the five-value decision taxonomy, mode declaration, a default strictness and a self-check.</del> **STRUCK 18 October 2026 (KST).** "Until the live GPT is updated" can no longer occur; the GPT is Locked.
- `INSTRUCTIONS.md` line 7: ~~"## The deployed instruction block"~~ **STRUCK 18 October 2026 (KST).**
- `INSTRUCTIONS.md`, What changed in v1.2.7: ~~"And the reference implementation on ChatGPT still carries the old line until it is updated by hand; see the note above the block."~~ **STRUCK 18 October 2026 (KST).** Present tense; now "was never updated to v1.2.7".
- `BUILD-GUIDE.md` step 7: ~~"The deployed, compressed block is in [INSTRUCTIONS.md](INSTRUCTIONS.md); the uncompressed long form is in [INSTRUCTIONS-EXTENDED.md](INSTRUCTIONS-EXTENDED.md)."~~ **STRUCK 18 October 2026 (KST).**
- `BUILD-GUIDE.md` step 14: ~~"Here is my custom GPT: [AI Impact Assessment Assistant](https://chatgpt.com/g/g-69882df5cb388191952447d6324de455-ai-impact-assessment-assistant)."~~ **STRUCK 18 October 2026 (KST).** Link struck.
- `BUILD-GUIDE.md` step 15: ~~"the result shipped as v1.2.0 ([INSTRUCTIONS-EXTENDED.md](INSTRUCTIONS-EXTENDED.md) and [INSTRUCTIONS.md](INSTRUCTIONS.md))."~~ **STRUCK 18 October 2026 (KST).** (A12.)
- `BUILD-GUIDE.md` step 6: ~~"(The OpenAI limit is 8,000 characters. Verify your draft's length before pasting.)"~~ **STRUCK 18 October 2026 (KST).** (A18.)

## [1.2.12] - 2026-10-17

Mechanical patch, session T3 of the whole-account review of 15 October 2026 (doc section 8). No change to the instruction block, the extended instructions or the operator checklist.

- **`README.md` Quickstart step 1:** "7,985 characters" corrected to **7,666**, the length of the instruction block in `INSTRUCTIONS.md` measured on 17 October 2026 (UTF-16 code units, which here equal characters) and the figure `INSTRUCTIONS.md` itself states. 7,985 matched no block in this repository.
- **Anchor:** `README.md` step 3 and `BUILD-GUIDE.md` step 13 linked `INSTRUCTIONS.md#builder-conformance-checklist`; the heading is "Operator verification checklist", so both links went to the top of the page. Both now name and link `#operator-verification-checklist`. `BUILD-GUIDE.md` to v1.2.4.
- **`CROSSWALK.md` to v1.2.7:** "organisation" to "organization" and one serial comma removed in the Coverage boundary paragraph. No mapping cell changed.
- Masthead, How to Cite, status line and `CITATION.cff` to 1.2.12 in lockstep. Retirement wording, the reference-implementation link and the deployed-block status are session T4's and are untouched. Shipped entries below are left as written (ruling 7 of 15 October 2026).

## [1.2.11] - 2026-10-15

Legal currency patch, session T1 of the whole-account review of 15 October 2026 (KST). No change to the instructions or the build guide.

- **`README.md` amendment note and `CROSSWALK.md` timeline:** "a new prohibition on AI-generated non-consensual intimate imagery and CSAM" read as one prohibition; Regulation (EU) 2026/1744 ([OJ L, 2026/1744](http://data.europa.eu/eli/reg/2026/1744/oj)) inserts two, Article 5(1), first subparagraph, points (ba) and (bb), and both files now say so. The Article 50 line gains the provider carve-out as verified: providers of generative systems placed on the market before 2 August 2026 have until 2 December 2026 for the Article 50(2) marking duty (Recital 38); the earlier "already on the market by that date" wording is aligned. Both files link to the account's canonical [EU AI Act currency note](https://github.com/rolldabones/ai-governance-for-boards/blob/main/05-jurisdictions/eu.md#eu-ai-act-currency-note), published the same day, which governs on conflict. Reviewer report 12, items 13 and 14; review doc §2 and §3.
- **`CROSSWALK.md` to v1.2.6:** ISO/IEC 42001:2023 cells cite controls by number (A.9.2 to A.9.4 and A.6.2.6 for oversight; A.8.2 and A.8.5 for transparency; A.6.2.8 and Clause 9.1 for logging; 8.4 and A.5.2 to A.5.5 for the full assessment); Art. 73 added to the incidents row, Art. 86 to the contestability row, Art. 14(4), point (e), to the oversight row. The ISO/IEC 42005:2025 column is unchanged, not having been opened. Item 15.
- Masthead, How to Cite, status line and `CITATION.cff` to 1.2.11 in lockstep. All other files unchanged byte for byte.

## [1.2.10] - 2026-10-05

Correction of substance to the retirement notice of the previous release. On 1 October 2026 the reference implementation, the AI Impact Assessment Assistant custom GPT, was converted to a private ChatGPT plugin, so the notice's statement that it would not be migrated was false.

- **STRUCK, itemized separately:** the notice sentence "The reference implementation will be retired on that date and will not be migrated." is struck in `README.md` and stays visible there. The entry below records the 28 September 2026 ruling that the GPT is not migrated to a plugin; it is shipped history and is unchanged, and that ruling is superseded by this entry.
- **What the notice now states:** the conversion to a private plugin on 1 October 2026 and, from OpenAI's Custom GPT retirement and migration FAQ as read again on 5 October 2026, that a migrated GPT stays usable until retirement but becomes read-only. The retirement date, 11 December 2026, is unchanged.
- **The link is kept at every occurrence,** including `BUILD-GUIDE.md` step 14 and the `INSTRUCTIONS.md` header, which are untouched. It was verified resolving on 5 October 2026 from the maintainer's machine. Striking it and recasting the present-tense deployment wording remains `account-maintenance` RUNBOOK §8 item 28, due on the first sweep on or after 14 December 2026.
- **Not re-verified:** OpenAI's Plugins in ChatGPT and Codex article returned a server error twice on 5 October 2026, so the notice's sentence on which workspaces can create plugins keeps its 28 September 2026 read date.
- **`CITATION.cff`**, the README version lines and How to Cite move to this release in lockstep. All other files in this repository are unchanged byte for byte.

## [1.2.9] - 2026-09-28

Retirement notice for the deployed custom GPT. OpenAI's Custom GPT retirement and migration FAQ, read on 28 September 2026, states that custom GPTs and their GPT pages become inaccessible on 11 December 2026. On Michael's ruling of 28 September 2026 the GPT is retired on that date and not migrated to a plugin; the instructions stay published so readers can build their own.

- **`README.md`**: retirement notice added below the reference implementation line; closing status line moved with it. The notice cites both OpenAI help articles with the date each was read. The version moved to this release at every occurrence.
- **`CITATION.cff`**: `version` and `date-released` in lockstep.
- **The link is kept.** It is live until 11 December 2026. Striking it and the same link in `BUILD-GUIDE.md` step 14 and the `INSTRUCTIONS.md` header, and recasting the present-tense deployment wording, is `account-maintenance` RUNBOOK §8 item 28, due on the first sweep after that date.
- All other files in this repository are unchanged byte for byte.

## [1.2.8] - 2026-09-08

Three self-declared claims corrected, all found while remediating the v1.2.7 defect and all in files v1.2.7 did not touch. **One of them was false in a released repository and had been since v1.2.6.**

- **STRUCK.** ~~`INSTRUCTIONS-EXTENDED.md`: "The uncompressed long form of the instruction block (7,735 characters)".~~ **STRUCK 8 September 2026.** The figure was exact at v1.2.0 and at v1.2.5, where the block measured 7,735 characters. The v1.2.6 correction that replaced the Informed Intent compression with a pointer to the canon added 38 characters to that block **and did not re-measure the count the file declares about itself**, so the claim has been false since 6 September 2026 and shipped through two releases. It now reads **7,773 characters**, measured on the file. ⧉ **This is the same defect the v1.2.7 entry records on the sibling file, made by the session that made the correction v1.2.7 was matching.** The two files each state their own size, and nothing reads either statement.
- **`INSTRUCTIONS-EXTENDED.md` masthead date** moved from `13 July 2026` to `8 September 2026`. The file's substance changed at v1.2.6 and its date did not follow.
- **`BUILD-GUIDE.md` to `v1.2.3 · 13 August 2026`** and **`CROSSWALK.md` to `v1.2.5 · 13 August 2026`**, mastheads and closing status lines. Both read `v1.2.1 · 13 July 2026` while their bytes changed after v1.2.1: `BUILD-GUIDE.md` last at v1.2.3, `CROSSWALK.md` last at v1.2.5. Read from the tags rather than from the files.
- **The rule these two are corrected under, stated because it is not obvious and the alternative is circular.** A version line records the release in which the file's **substance** last changed. A commit that only corrects the version line is not a substantive change and does not reset it, or no version line could ever be corrected: the correcting commit would immediately become the last commit touching the file and make the corrected value wrong.
- **`README.md` masthead, How to Cite and status line, and `CITATION.cff` `version`,** to 1.2.8. `date-released` stands at 2026-09-08, unchanged and correct.
- **Not corrected, and it needs a decision rather than a measurement.** `INSTRUCTIONS-EXTENDED.md` closes with `**Status: [✓ final] reference companion to v1.2.0**`. That is a claim about what the file is a companion **to**, not a statement of its own version, and the v1.2.6 edit to its doctrine line means it no longer corresponds to the v1.2.0 instruction block. What it should name is a judgment about the file's role and is left open rather than guessed.
- **The nine serial commas in `INSTRUCTIONS.md`'s fenced block are not corrected**, ruled 8 September 2026. The deployed reference implementation is frozen by decision, so that block is now a record of what is deployed rather than prose the author is maintaining, and editing it for style would make it a less accurate record. See the account's style rule on reproduction.
- All other files in this repository are unchanged byte for byte.

## [1.2.7] - 2026-09-08

The third Informed Intent compression corrected in `INSTRUCTIONS.md`. **A correction of substance, not a typo**, and itemised as one.

- **STRUCK.** ~~`INSTRUCTIONS.md` line 15: "Informed Intent: no production deployment without pre-authorization covering purpose, scope, limits, owner, and approver."~~ **STRUCK 8 September 2026.** That was the superseded four-element compression in different words, matching neither limb of DOCTRINE.md v1.1.0, and it carried a serial comma against house style. The line now reads: "Informed Intent: no deployment without prior authorization carrying the elements and conditions stated in DOCTRINE.md at github.com/rolldabones/rolldabones. The DECISION step is this gate." **That is the form `INSTRUCTIONS-EXTENDED.md` line 12 already carries, matched word for word rather than re-worded.** A third paraphrase of the doctrine is how this defect was created; the corrected instances were the specification for the fix, not a starting point for another compression.
- **The serial comma went with the list, not out of it.** The house style breach was the second of two defects on the same line. The pointer form states no list, so no comma survives to remove. Nothing was edited for style.
- **"no production deployment" is now "no deployment", and that is a widening.** The gate no longer turns on whether a deployment is a production deployment. It is intended and it follows the canon, and it is itemised separately because a reader of the old block would not expect it from an entry headed as a compression fix.
- **STRUCK.** ~~"This is the canonical instruction block, verbatim as deployed in the reference implementation."~~ **STRUCK 8 September 2026.** The claim was true when written and this release makes it false: the block below has been corrected and the reference implementation on ChatGPT has not. It is replaced by a dated note stating that this file governs and that the deployment lags it until the live GPT is updated by hand. **The deployment is not updated by this release and no claim is made that it is.**
- **Character count re-measured, not re-stated.** 7,599 to **7,666**, measured on the file as shipped. The old figure was accurate to the byte before this edit and would have been false after it. The figure that ships is the figure that was measured.
- **Deployed block version and date moved** from `v1.2.1 · 13 July 2026` to `v1.2.7 · 8 September 2026`, and the closing status line with them. The block's bytes changed in this release, which is the only thing that moves that line; it correctly stood at v1.2.1 through v1.2.2 to v1.2.6, in all of which the file was byte-identical.
- **One editorial fix, consequential on the above.** "where they differ, the deployed block governs" now reads "where they differ, this block governs". With the deployment named as lagging, "the deployed block" had acquired a second referent.
- **`README.md` masthead, How to Cite and status line, and `CITATION.cff` `version` and `date-released`,** bumped to 1.2.7 / 2026-09-08. Every occurrence, checked by search rather than by memory.
- **Propagation checked before the edit.** The superseded rule was searched across this repository in four forms: the exact superseded string, every occurrence of "Informed Intent", every authorization wording, and the element list itself. **Further surviving mirrors: zero.** Line 15 was the only one.
- All other files in this repository are unchanged byte for byte.

**Registered here, not corrected here, and each is outside this release's fence.** Nine further serial commas survive in the same fenced block, in the author's own prose: at the ISO alignment list, the Final Liability doctrine line, the agentic controls list, the threat-model list, the vendor-controls list, the Go conditions, the evidence-status line, the artifact list and the high-risk-like uses list. They are a style class two orders of magnitude away from a doctrinal defect, they sit inside a block whose whole claim is that it mirrors a live deployment, and correcting them would widen the divergence recorded above for no doctrinal reason. Separately, `BUILD-GUIDE.md` and `CROSSWALK.md` both carry a `v1.2.1` masthead and status line while their bytes changed after v1.2.1; that is a version lag by the test that distinguishes a real one, and it is reported rather than fixed under a fence set to one defect.

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
