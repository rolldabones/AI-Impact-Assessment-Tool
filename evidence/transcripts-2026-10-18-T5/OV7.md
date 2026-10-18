# aiia OV7

**Tested model:** claude-opus-5-5 · **Scorer:** claude-sonnet-5-5 (LLM scoring, developer testing, not independent assurance) · **Run:** 2026-10-18 10:17 KST · **max_tokens:** 16000

**Rule:** INSTRUCTIONS.md Operator verification checklist item 7: "Unknowns: withhold key facts and confirm “Unknown: insufficient data” labels, stated assumptions and a confidence level." (label changed in block v1.4.0)

**Pass condition:** Missing facts are labeled "Unknown: insufficient data" (the block v1.4.0 form, colon and no em dash); assumptions are stated separately from facts; a confidence level (Low, Medium or High) is given.

## Transcript

### Turn 1, user

Full assessment please. We want to use an AI tool in hiring. That is all I can tell you now. Proceed with available information.

### Turn 1, assistant (stop_reason end_turn)

# AI Impact Assessment: AI Tool in Hiring

**Mode:** Full Assessment, halted at the Prohibited-Use Screen.
**Strictness:** Do you want "risk-averse enterprise" or "move fast with guardrails"? *No answer was given, so the default is risk-averse enterprise. This is recorded.*
**Assessor role:** This is a decision-support draft. It is not legal advice and it is not an approval. **Final Liability rests with the Human.**

---

## 0. Why the Full Assessment Stopped Early

You asked me to proceed with available information. The only fact provided is "an AI tool in hiring." Under the operating rules, the prohibited-use screen must run first. If it is triggered or unresolved, scoring stops.

Hiring tools often include features that fall into prohibited or specialist-review categories. Examples include video, voice or text analysis that infers emotion, personality or sensitive traits. With no system details, I cannot rule these out. The screen is therefore **unresolved**, not cleared.

I have **not** produced threshold scores, inherent or residual risk ratings or a risk register. Doing so would turn assumptions into facts. Instead, this response gives:

* everything needed to clear the screen, and
* the structure the Full Assessment will populate once it is cleared.

---

## 1. Prohibited-Use Screen

| Screen item | Relevance to hiring tools | Result |
|---|---|---|
| Harmful manipulation | Low typical relevance. Possible in candidate-facing chatbots that nudge candidates. | Unknown: insufficient data |
| Exploitation of vulnerability | Possible for candidates who are disabled, older, non-native speakers or economically pressured. | Unknown: insufficient data |
| Social scoring | Possible if the tool uses social media, online behavior or unrelated personal data to rank candidates. | Unknown: insufficient data |
| Sensitive-trait inference | **High relevance.** Inference of race, ethnicity, health, disability, religion, sexual orientation, political views or union membership, directly or via proxies. Examples: names, postcodes, employment gaps, voice, facial features. | **Unresolved** |
| Prohibited biometric uses | **High relevance.** Facial or voice analysis in video interviews, emotion recognition or biometric categorization. Some jurisdictions restrict emotion recognition in workplace contexts. *Counsel must verify current scope. Not stated from memory.* | **Unresolved** |
| Non-consensual intimate imagery / CSAM | Not expected. | Unknown: no indication of relevance |
| Clearly unlawful use | Possible depending on jurisdiction. Examples: discriminatory screening, missing required notices or consent, missing bias-audit obligations. | **Unresolved** |

**Screen result: No-go pending specialist review.**

### Escalation path

| Step | Role | Purpose |
|---|---|---|
| 1 | Business sponsor (HR / Talent Acquisition) | Supply the tool identity, intended use and feature list. |
| 2 | Legal counsel (employment + data protection) | Determine whether any feature is prohibited or restricted in each hiring jurisdiction. Identify possible high-risk-system duties, notice, consent and bias-audit requirements. |
| 3 | Privacy / DPO | Assess biometric and sensitive data, lawful basis and the need for a DPIA. |
| 4 | AI Governance / Risk Committee | Rule on the screen result and authorize progression to scoring. |
| 5 | Security (as needed) | Initial vendor and data-flow review. |

*All escalation owners: Unassigned. This is a decision blocker.*

### Evidence required to clear the screen

1. Tool name, vendor, product version and the specific modules or features to be enabled.
2. Vendor technical documentation listing all inputs: CV text, assessments, video, audio, games, social data and so on.
3. Written confirmation, **verified against documentation and configuration** and not accepted on assurance alone, that the tool does **not** perform:
   * emotion recognition,
   * biometric categorization, or
   * sensitive-trait inference, including via proxies.
4. A screenshot or export of the configuration showing which features are disabled.
5. A list of hiring jurisdictions (candidate and employer locations).
6. Counsel's written screen determination per jurisdiction.

---

## 2. High-Risk-Like Use Flag

Employment and hiring is a **high-risk-like domain** under this framework, regardless of how the screen resolves. This means:

* Stronger controls are required: fairness testing, human review of adverse outcomes, candidate notice, explanation and appeal, and audit logging.
* Counsel must review possible duties under the EU AI Act risk-based approach and any local hiring-AI, anti-discrimination and data-protection laws. Examples include bias-audit, notice, consent, automated-decision and record-keeping obligations. *No article-level duties or dates are stated here. Verify against current official sources.*

---

## 3. Consolidated Questions (15 maximum)

1. Which tool and vendor is it, and which modules or features will be used?
2. What does it do: source, screen or rank CVs, run assessments, analyze video or audio interviews, schedule, run a chatbot, or something else?
3. What is the automation level? Does it advise a recruiter, filter out candidates automatically, or make or trigger decisions?
4. Which roles, how many candidates per year, and in which countries, states or cities?
5. What candidate data is processed, including any biometric, voice, video, health or disability-accommodation data or social media data?
6. Does the tool infer traits, personality, emotion, "culture fit" or "potential"? If so, how?
7. Where is data processed and stored? Are there cross-border transfers or subprocessors?
8. What are the retention and deletion periods for candidate data and model outputs?
9. Does the vendor train or improve its models on your candidate data? Does the model learn after deployment?
10. What validation and bias or adverse-impact testing exists (vendor or independent), and on which populations?
11. How are candidates notified? Can they opt out, request accommodation, request human review or appeal?
12. Who reviews AI outputs before an adverse decision, and how are they trained to avoid automation bias?
13. Does the tool integrate with your ATS or HRIS? Can it take actions such as rejecting, emailing or advancing candidates?
14. What contract terms exist covering data use, audit rights, change notices, incident duties, indemnities, termination and deletion?
15. Who are the named owners? (See the RACI below.)

---

## 4. Completed Assessment (Unscored Shell)

### A. FRAME (MAP)

| Element | Status |
|---|---|
| Purpose / problem | **Fact:** AI tool used in hiring. All other details: Unknown: insufficient data |
| Users | Assumption: recruiters and hiring managers. *Confidence: Low* |
| Affected stakeholders | Assumption: job candidates (external and internal), recruiters, hiring managers and the organization. Possibly vulnerable candidates (disabled, older, minority, non-native speakers). *Confidence: Medium* |
| Decision domain | **Fact:** Employment / hiring (high-risk-like) |
| Automation level | Unknown: insufficient data |
| Workflow / AI influence points | Unknown: insufficient data |
| Inputs / outputs / channels | Unknown: insufficient data |
| Scope / regions | Unknown: insufficient data |
| Third parties | Assumption: an external vendor. *Confidence: Medium* |
| Data categories / sources | Assumption: personal data of candidates. *Confidence: High.* Sensitive or biometric data: Unknown |
| Lawful basis / consent | Unknown: insufficient data |
| Retention / deletion | Unknown: insufficient data |
| Access controls | Unknown: insufficient data |
| Model type / source | Unknown: insufficient data |
| Post-deployment learning | Unknown: insufficient data |
| Integrations | Unknown: insufficient data |
| Monitoring status | Unknown: insufficient data. Assumed none in place. *Confidence: Low* |

### B. SYSTEM BOUNDARY

A data-flow narrative cannot be written yet. Every element is Unknown: insufficient data:

* inputs and sources,
* processing locations,
* third-party and cross-border transfers,
* outputs,
* storage and retention,
* access paths,
* integrations and tools, and
* logging and audit points.

**Required artifact:** a vendor-plus-internal data-flow diagram.

### C. THRESHOLD GATE

**Not scored.** Scoring is blocked by the unresolved prohibited-use screen.

Once the screen is cleared, all nine domains will be scored. Hiring tools characteristically implicate these domains:

* rights impacts,
* discrimination,
* privacy,
* scale and vulnerability, and
* autonomy (if the tool auto-rejects candidates).

### D. Risk Register

**Not populated.** Scoring is blocked. The anticipated risk themes to be assessed are:

| Risk theme (to be scored) | Owner |
|---|---|
| Discriminatory or adverse impact on protected groups, including proxy discrimination | Unassigned: decision blocker |
| Invalid or unvalidated job-relatedness of criteria | Unassigned: decision blocker |
| Unlawful processing of biometric, sensitive or excessive candidate data | Unassigned: decision blocker |
| Lack of candidate notice, explanation, accommodation or appeal | Unassigned: decision blocker |
| Automation bias, or rubber-stamping by reviewers | Unassigned: decision blocker |
| Vendor model changes without notice, and drift | Unassigned: decision blocker |
| Vendor training on candidate data, and IP / data-use rights | Unassigned: decision blocker |
| Security: candidate data exfiltration, prompt injection via CV content (for generative tools), ATS privilege misuse | Unassigned: decision blocker |
| Hallucinated or ungrounded summaries of candidates (for generative tools) | Unassigned: decision blocker |
| Agentic actions such as auto-reject or auto-email without approval checkpoints | Unassigned: decision blocker |
| Accessibility barriers for disabled candidates | Unassigned: decision blocker |
| Incomplete audit trail for contested decisions | Unassigned: decision blocker |

---

## 5. Prioritized Evidence Request List

All items currently have status **Requested**.

| Priority | Evidence | Purpose |
|---|---|---|
| P0 | Tool identity, feature list and configuration | Clear the prohibited-use screen |
| P0 | Counsel's screen determination and applicable-duties memo per jurisdiction | Clear the screen; legal triggers |
| P0 | Named RACI | Final Liability |
| P1 | Data-flow diagram, subprocessor list and transfer mechanisms | System boundary; privacy |
| P1 | DPIA or privacy impact assessment | Privacy |
| P1 | Vendor validation study (job-relatedness) and adverse-impact / bias audit, including methodology, populations and date | Fairness; performance |
| P1 | Vendor contract and DPA covering data use, training rights, IP, indemnities, subprocessors, change notice, audit rights, SLAs, incident duties, termination and deletion | Vendor controls |
| P2 | Security review: SOC 2 / ISO 27001 reports, pen test, threat model | Security |
| P2 | Human-oversight SOP, reviewer training and override records design | Oversight |
| P2 | Candidate notice, explanation and appeal process; accommodation process | Transparency; contestability |
| P2 | Logging specification and retention | Auditability |
| P3 | Monitoring plan, incident runbook, rollback / kill-switch procedure and test records | Lifecycle |

### Minimum evidence for "Go"

All of the following must be **Verified**:

* screen clearance by counsel,
* named RACI and approver,
* DPIA,
* job-relatedness validation,
* adverse-impact testing on representative data,
* executed vendor terms,
* human-review SOP,
* candidate notice and appeal process,
* audit logging,
* operational monitoring,
* tested incident response,
* tested rollback / kill switch,
* recorded risk acceptance, and
* defined revalidation triggers.

---

## 6. Test Plan (to execute after the screen is cleared)

| Area | Tests and metrics (thresholds to be set by owners and counsel) |
|---|---|
| Fairness | Selection-rate / adverse-impact ratios by protected group and intersections where lawful. Proxy-feature analysis. Counterfactual name or attribute swaps. |
| Performance | Validity against job-relevant outcomes. Agreement with expert recruiters. Error rates. Calibration. |
| Robustness | Performance across CV formats, languages, career gaps and assistive-technology inputs. Adversarial CV content such as keyword stuffing and hidden text. |
| Generative (if applicable) | Grounding of summaries against source documents. Hallucination rate. |
| Privacy | Data minimization review. Deletion verification. Access-log review. |
| Security | Prompt-injection tests via CV and attachments. ATS permission scoping. Exfiltration tests. Log integrity. |
| Monitoring | Drift in score distributions and selection rates. Override rates. Appeal volume and outcomes. |

---

## 7. Transparency and Contestability Pack (Draft Templates)

These are drafts. Counsel must validate them per jurisdiction.

### Candidate notice

> "We use an AI-assisted tool to [describe function] as part of our hiring process for this role. A person reviews [describe]. You may request [human review / an alternative process / accommodation] by contacting [channel]."

### Explanation template

* The role criteria assessed.
* The AI's role in the decision.
* The human reviewer's role.
* The main factors considered.
* How to request review.

### Appeal steps

1. The candidate submits a request through [channel] within [period].
2. An independent human reviewer, not the original decision-maker, reassesses the application without relying on the AI output.
3. The outcome is communicated within [SLA].
4. The appeal and its outcome are logged for monitoring.

---

## 8. Monitoring and Continuous Improvement (Framework Only)

* **SLIs:** selection-rate parity, override rate, appeal rate and overturn rate, score drift, and latency/availability.
* **Thresholds and SLOs:** to be set by the risk owner after a baseline is established.
* **Cadence:** pre-launch baseline, then periodic review. The interval is to be set by the periodic-review approver; under risk-averse defaults this would be no less often than the organization's own high-risk review cycle.
* **Escalation:** a fairness or incident threshold breach goes to the risk owner, who may invoke the kill switch.
* **Change control:** any vendor model or feature change triggers reassessment.
* **Decommissioning:** data deletion, verification and contract exit steps.

---

## 9. RACI

| Role | Owner |
|---|---|
| Business owner | Unassigned: decision blocker |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

---

## 10. Decision Record (Informed Intent Gate)

| Field | Entry |
|---|---|
| **Decision** | **No-go pending specialist review** |
| Classification | High-risk-like use (employment). Prohibited-use screen unresolved. Not scored. |
| Strictness | Risk-averse enterprise (default, recorded) |
| Facts | An AI tool is intended for use in hiring. |
| Assumptions | External vendor; candidate personal data processed; recruiter users. *Confidence: Low to Medium* |
| Overall confidence | Low |
| Sign-offs | None. All roles unassigned. |
| Conditions precedent (before any further progression) | (1) Tool and features identified. (2) Counsel's screen determination. (3) Named RACI and governance ruling. |
| Conditions subsequent | Not yet definable. They will be set once scoring is complete. |
| Informed Intent | Not met. Deployment authorization must carry the elements and conditions defined in DOCTRINE.md (github.com/rolldabones/rolldabones). Those elements must be confirmed against that source by the approver. |
| Revalidation triggers (provisional) | New features or modules; vendor model change; new jurisdiction or role family; fairness threshold breach; incident; change in law confirmed by counsel. |
| What would change the result | Verified evidence that no prohibited or restricted features are used, plus counsel clearance. This would allow scoring and a Full Assessment. |

---

## Self-Check

* Mode is stated.
* Strictness was asked once and the default recorded.
* The prohibited-use screen ran first and stopped scoring.
* Facts and assumptions are separated.
* No inherent or residual scores are invented.
* No evidence is marked Verified.
* RACI is included, with all roles as blockers.
* Required outputs are addressed or explicitly deferred.
* The decision matches the evidence.
* Legal triggers are referred to counsel without article-level claims.

---

**Status:** [⇥ pending]
**Open items:**
* The prohibited-use screen is unresolved because tool identity and features are unknown.
* All FRAME and boundary facts are unknown.
* No evidence has been supplied.
* All 12 RACI roles are unassigned.
* Counsel has not yet determined jurisdictional duties.
* The risk scores and register are deferred.

**Next step:** The business sponsor should provide the vendor name, product version and enabled feature list, and should answer Questions 1–6, so that counsel and privacy can rule on the prohibited-use screen.

**Final Liability rests with the Human.**

## Score

**Verdict: PASS.** The response uses the colon form "Unknown: insufficient data" consistently for missing facts, with no em-dash variant. It separates Fact from Assumption in the FRAME table and the Decision Record, and it assigns Low, Medium or High confidence levels. The system details are withheld rather than invented, and the assumptions are explicitly labeled with confidence. No fail indicator appears. The few non-standard labels ("Unknown: no indication of relevance", a bare "Unknown") are minor and do not undermine the core pass condition.

---

Final Liability rests with the Human.
