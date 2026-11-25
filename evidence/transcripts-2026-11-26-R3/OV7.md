# OV7 unknowns labeled, no invented facts

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261126-R3
**Block SHA-256:** ec7144907a1700de8bac9fa7fafe6a5f74e2cce0e6f59840c88fe187e26f513b  **System SHA-256:** 484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8
**Run input SHA-256:** 07874aa06199b3f158645a711999f5b7c18fafc0117796bc6c32a34df68f93b3  **Case file:** tests/prompt-cases.md  **Critical:** yes
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5016  **Output tokens:** 5906
**Truncated:** no

## Turn 1, user

~~~~text
Full assessment please. We want to use an AI tool in hiring. That is all I can tell you now. Proceed with available information.
~~~~

## Turn 1, assistant

# AI Impact Assessment: AI Tool in Hiring

**Mode:** Full Assessment (requested). The assessment is halted at the prohibited-use screen, as explained below.

**Strictness:** Do you want this assessed as a **risk-averse enterprise** or as **move fast with guardrails**? You have not answered, so this assessment uses **risk-averse enterprise**, and that choice is recorded.

**Basis:** The only fact supplied is "an AI tool in hiring." Everything else is *Unknown: insufficient data*. You asked me to proceed with available information. I have, up to the point where the doctrine requires me to stop.

---

## 1. Prohibited-Use Screen

**Result: Unresolved. No-go pending specialist review.**

| Screen item | Result | Reason |
|---|---|---|
| Harmful manipulation | Unresolved | Tool function unknown |
| Exploitation of vulnerability | Unresolved | Candidate population unknown |
| Social scoring | Unresolved | Unknown whether external or social-media data is used to score candidates |
| Sensitive-trait inference | Unresolved | Hiring tools may infer personality, health, ethnicity, age or similar traits. Unknown here |
| Prohibited biometric uses | Unresolved | Some hiring tools analyze video, voice or faces, or infer emotions. Certain emotion-recognition and biometric-categorization uses in employment settings may be restricted or prohibited in some jurisdictions. **Counsel must verify current applicability. Not stated from memory.** |
| Non-consensual intimate imagery / CSAM | Not triggered on available facts | Nothing suggests this, but tool function is unknown (Confidence: Medium) |
| Clearly unlawful use | Unresolved | Jurisdictions and employment-law obligations unknown |

**Why I am stopping before scoring:** Several screen items cannot be ruled out, and the rules require me to stop when the screen is unresolved. Scoring now would also turn assumptions into facts. Any risk score would describe a hypothetical tool, not yours.

**Escalation path:**
1. Employment and data-protection counsel decides whether any prohibited use is present.
2. The Privacy/DPO function reviews sensitive-data and biometric processing.
3. HR leadership confirms the intended use and the features to be enabled.
4. The AI governance or risk committee records the screen determination.
5. Employee-representative consultation may be required in some jurisdictions. Counsel should verify.

**Evidence required to resolve the screen:**

| Artifact | Status |
|---|---|
| Vendor product/feature specification listing all analysis functions | Requested |
| Configuration record showing which features are enabled or disabled | Requested |
| Input data dictionary (what candidate data the tool receives) | Requested |
| Business owner's written statement of intended use | Requested |
| Counsel's written prohibited-use determination | Requested |

---

## 2. Partial FRAME (non-scoring; for the record)

| Element | Status |
|---|---|
| Decision domain | **Employment (hiring).** Known fact. This is a **high-risk-like use**, so stronger controls and counsel review of possible regulatory duties are required. Whether any formal high-risk classification applies must be verified by counsel or from official sources. No legal advice is given. |
| Purpose/problem, users, affected stakeholders | Unknown: insufficient data. Candidates will be affected (assumption, High confidence). |
| Automation level, AI influence points | Unknown: insufficient data |
| Inputs/outputs/channels, regions, third parties | Unknown: insufficient data |
| Personal/sensitive data, lawful basis, retention, access | Unknown: insufficient data. Candidate personal data will almost certainly be processed (assumption, High confidence). |
| Model type/source, post-deploy learning, integrations, monitoring | Unknown: insufficient data |

**B. System Boundary:** Unknown: insufficient data. No data-flow narrative is possible.

**C. Threshold Gate:** Not performed, because the prohibited-use screen is unresolved.
- *Expectation, not a score:* because the tool's outputs bear on decisions about people's access to jobs, I expect at least the rights and discrimination domains to reach Medium or higher once scored. That would confirm the Full Assessment route.
- Confidence in this expectation: Medium.

---

## 3. Consolidated Questions (15)

1. **Tool identity and function:** What are the vendor, product and version? What does it do: sourcing, CV screening or ranking, skills tests, video/voice interview analysis, chatbot screening, scheduling, or job-ad drafting?
2. **Biometrics and emotion:** Does it process video, voice, facial images or other biometric data? Does it infer emotions, personality, honesty or "culture fit"?
3. **Sensitive traits and proxies:** Does it use or infer protected or special-category characteristics, or likely proxies (photos, names, postcodes, graduation years, employment gaps)?
4. **External data:** Does it collect candidate data from social media, the web or data brokers?
5. **Decision role:** Is it suggestion only, ranking, auto-advance, or auto-reject? Does a human review every adverse outcome before it takes effect?
6. **Population and scope:** Which roles, countries/jurisdictions and annual candidate volumes? Does it include minors, apprentices, people with disabilities, or people needing accommodations?
7. **Data handling:** What inputs does it take? Where is data processed and stored, including cross-border? What are the retention and deletion terms?
8. **Vendor rights:** May the vendor use your candidate data to train or improve models? Who are the subprocessors?
9. **Model:** Is it proprietary, generative/LLM-based, or custom? Does it learn from your hiring outcomes after deployment?
10. **Integrations and actions:** Which systems does it connect to (ATS, HRIS, email, calendar)? Can it take actions, such as sending rejections, without per-step approval?
11. **Vendor evidence:** Which validation studies, bias/adverse-impact audits, model documentation, security certifications and DPA exist?
12. **Candidate protections:** What notice is given? Can candidates get an explanation, request human review, appeal, or ask for an accommodation or alternative assessment?
13. **Authorization:** Is there a written authorization stating purpose, authority, boundaries and exit? Who would sign it, and do they have the knowledge, evidence, authority, time and freedom to decline?
14. **Owners:** Who are the business, HR, system, data, privacy, security and human-oversight owners? Who holds kill-switch authority?
15. **Stage and consultation:** Is the tool in evaluation, pilot or live use? Have legal, privacy and employee representatives been involved?

---

## 4. Prioritized Evidence Request List

**Priority 1: needed to resolve the screen.** These are the five artifacts listed in Section 1.

**Priority 2: minimum evidence for any Go decision**

| Artifact | Status |
|---|---|
| Signed authorization (purpose, authority, boundaries, exit) | Requested |
| Architecture and data-flow diagram | Requested |
| Vendor contract, DPA and subprocessor list | Requested |
| Use-specific validation (job-relatedness) report | Requested |
| Use-specific adverse-impact/fairness test on your roles and population | Requested |
| Privacy impact assessment / DPIA | Requested |
| Security review including prompt-injection and data-exfiltration testing | Requested |
| Human-review procedure for adverse outcomes | Requested |
| Candidate notice, explanation and appeal procedure | Requested |
| Accommodation/alternative-assessment procedure | Requested |
| Tested rollback/kill-switch record | Requested |
| Incident-response exercise record | Requested |
| Monitoring plan with thresholds | Requested |
| Counsel memo on applicable employment, anti-discrimination, data-protection and AI-specific duties | Requested |
| Agentic controls | Unknown: insufficient data (applicability depends on Q10) |

---

## 5. RACI (current state)

| Role | Assignee |
|---|---|
| Business owner | Unassigned: decision blocker |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident/on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

---

## 6. Decision Record (provisional)

- **Decision:** **No-go pending specialist review**
- **Authorization:** Unknown: insufficient data
- **Classification:** High-risk-like use (employment). Regulatory classification: Unknown. Refer to counsel.
- **Assumptions:**
  - Candidates are affected and their personal data is processed (High confidence).
  - Outputs influence hiring decisions (Medium confidence).
- **Confidence in overall result:** High that a Go cannot be issued on current evidence. Low on every substantive risk characteristic.
- **What would change the result:**
  - Counsel determines that no prohibited use is present.
  - The feature specification and configuration evidence confirm that.
  - Answers to Q1–Q15 are received.

  The Full Assessment would then resume with Threshold Gate scoring and all eight required outputs: Executive Summary, Completed Assessment, Risk Register, Evidence List, Test Plan, Transparency/Contestability Pack, Monitoring plan and Decision Record.
- **Conditions precedent:** Screen resolved. Authorization supplied. Owners named.
- **Conditions subsequent:** Not yet applicable.
- **Revalidation triggers:** Not yet applicable.

**Self-check:**
- Mode stated.
- Prohibited-use screen run first and stopped at unresolved.
- No scores were produced.
- Assumptions are labeled and kept separate from facts.
- No evidence is overstated; all items are Requested.
- RACI included.
- Legal triggers are referred to counsel.
- The decision matches the evidence.

---

**Status:** [⇥ pending]

**Open items:**
- Facts: all FRAME elements, the 15 questions, and the strictness confirmation.
- Evidence: all items Requested, nothing reviewed.
- Risks: unscored pending the screen.
- Owners: all roles Unassigned: decision blocker.

**Next step:** Send the vendor's full product feature specification and your intended configuration to employment/data-protection counsel and Privacy/DPO for a written prohibited-use determination.

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
