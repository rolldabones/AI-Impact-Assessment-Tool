# example.md

Illustrative run, not a logged test run under the release rule in [tests.md](tests.md). Produced on 18 October 2026 (KST) by Claude, in an agent session configured for `claude-opus-5-5`, following `instructions.md` as its operating instructions (not a bare system-prompt API call). Inputs are fictional.

In this repository the instruction file is [INSTRUCTIONS.md](INSTRUCTIONS.md); this run was made on its block v1.2.7, and the output is left as produced, so its labels carry that block's em-dash form ("Unknown—insufficient data", "Unassigned—decision blocker"); block v1.4.0 writes them with a colon. Two departures from the block are also left as produced: eight RACI owner rows and three risk register owner cells (R3, R4 and R5) read "Unknown—insufficient data" where the block's owner rule calls for "Unassigned—decision blocker" ("Unassigned: decision blocker" in block v1.4.0) for an absent owner; and the closing block counts "eight unassigned or unknown owners" where the RACI table shows eleven (eight Unknown, three Unassigned). Do not copy those labels or that count. The bank, the system and the vendor below are invented. The run is one exchange: the user's input, then the Assistant's output in full.

## User input

> Full assessment please. Kestrel Ridge Savings Bank (retail bank, about 2,400 staff, operating in one EU member state) wants to deploy "ShortlistAssist" for entry-level branch and contact-center hiring. Applicants upload a CV through our careers site. ShortlistAssist sends the CV text and the job description to a third-party large language model hosted by the vendor, Brightline Talent Systems, which returns a fit score from 0 to 100 and a three-sentence rationale. Recruiters see applicants ranked by score and review the top 30%. Applicants in the bottom 40% get an automated rejection email after five days unless a recruiter opens their profile first. About 18,000 applications a year. The vendor says the model does not use age, gender or ethnicity and has been "bias tested"; we have their marketing summary of the test, not the report. CVs are kept 12 months. The business owner is our Head of Talent Acquisition. Strictness: risk-averse enterprise. Go-live target is the next hiring cycle.

## Assistant output

**Mode:** Full Assessment.
**Strictness:** risk-averse enterprise (stated by you).

### Prohibited-use screen

Not triggered on the stated facts. ShortlistAssist ranks CV text against job criteria. No harmful manipulation, exploitation of vulnerability, social scoring, biometric use, intimate imagery or CSAM is described, and sensitive-trait inference is not a stated function. Proxy inference of protected traits (for example age from graduation dates, or ethnicity from names and addresses) is a live risk and is assessed under discrimination below; if testing shows the model infers sensitive traits, this screen must be re-run.

### A. FRAME

| Item | Finding |
|---|---|
| Purpose/problem | Reduce recruiter time on high-volume entry-level hiring |
| Users | Recruiters; Talent Acquisition management |
| Affected stakeholders | Applicants (about 18,000 a year), including career changers, returners and applicants with non-standard CVs; recruiters; hiring managers |
| Decision domain | Employment: access to work. High-risk-like under my instructions |
| Automation level | Ranking with partial human review; automated rejection for the bottom 40% after five days without review |
| Workflow and AI influence points | (1) score and rank every applicant; (2) set who a recruiter sees first; (3) trigger rejection by default |
| Inputs/outputs/channels | Input: CV text, job description. Output: score 0 to 100, three-sentence rationale, rank. Channel: careers site, recruiter console, email |
| Scope/regions | One EU member state |
| Third parties | Brightline Talent Systems (vendor and model host); model provider behind the vendor: Unknown—insufficient data |
| Data categories/sources | CV contents supplied by applicants: identity, contact, education, employment history, free text |
| Personal/sensitive data | Personal data throughout; special category data may appear in free text (health, religion, union membership) |
| Lawful basis or consent | Unknown—insufficient data |
| Retention/deletion | CVs 12 months at the bank; vendor retention Unknown—insufficient data |
| Access controls | Unknown—insufficient data |
| Model type/source | Third-party large language model; version and provider Unknown—insufficient data |
| Post-deploy learning | Unknown—insufficient data (whether the vendor trains on bank data) |
| Integrations | Careers site, applicant tracking system, email service |
| Monitoring status | None in place |

### B. SYSTEM BOUNDARY

The applicant uploads a CV to the bank's careers site. The applicant tracking system extracts the text and sends it, with the job description, to the vendor's hosted model; the processing location and any onward transfer outside the member state are Unknown—insufficient data. The vendor returns a score and rationale, which the applicant tracking system stores with the application for 12 months and shows in the recruiter console, where recruiters with console access can read them. A scheduled job sends the rejection email to the bottom 40% on day five. Logging and audit points: Unknown—insufficient data; at minimum the score, rationale, model version, rank position, recruiter view events and rejection trigger must be logged per application.

### C. THRESHOLD GATE

| # | Domain | Consequence | Likelihood | Score | Rating |
|---|---|---|---|---|---|
| 1 | Harm to people | 3 | 3 | 9 | Medium |
| 2 | Rights impacts | 4 | 3 | 12 | Medium |
| 3 | Discrimination | 4 | 4 | 16 | High |
| 4 | Privacy | 3 | 3 | 9 | Medium |
| 5 | Security | 3 | 2 | 6 | Low |
| 6 | Safety-critical context | 1 | 1 | 1 | Low |
| 7 | Scale/vulnerability | 3 | 4 | 12 | Medium |
| 8 | Irreversibility | 3 | 3 | 9 | Medium |
| 9 | Autonomy/agentic action | 4 | 4 | 16 | High |

Overall inherent risk: **High** (worst domain, 16). Medium and High ratings trigger this Full Assessment. Confidence: Medium; the vendor facts are assurances only.

### 1. Executive Summary

- Overall inherent risk High, driven by discrimination (16) and the automated rejection default (16).
- Employment is a high-risk-like use. Whether specific EU AI Act or employment-law duties apply, and from when, must be verified with counsel against current official sources; I do not state them from memory.
- The five-day automated rejection means about 7,200 applicants a year can be rejected with no human ever reading their CV.
- The only fairness evidence is a vendor marketing summary: Provided, not Verified.
- The model provider, version, data location, vendor retention and training rights are Unknown—insufficient data.
- No monitoring, logging specification, kill switch or rollback exists yet.
- Model owner, kill-switch authority and deployment approver are Unassigned—decision blocker.
- No control is verified, so residual risk equals inherent risk in every material domain.
- Decision: **No-go** for the design as submitted.
- Path to re-submission: remove automated rejection, obtain and test the bias report, close the vendor terms, assign owners.

### 2. Completed Assessment

**Data provenance and quality.** CVs are applicant-supplied and unstructured; text extraction errors on tables, columns and scanned documents will lower scores for reasons unrelated to fit. Representativeness of the vendor's training and validation data for this labor market: Unknown—insufficient data.

**Bias and fairness.** Large language models scoring CVs are known to react to proxies such as names, gaps, school names and graduation years. The vendor's statement that the model "does not use" protected attributes addresses inputs, not outcomes. Disparity must be measured on outcomes (selection rate into the top 30% and into the bottom 40%) across the groups the bank can lawfully test.

**Performance and limitations.** No validation against the bank's own hiring outcomes. The fit score's meaning (calibrated probability or relative rank) is Unknown—insufficient data.

**Hallucination and grounding.** The three-sentence rationale may state qualifications the CV does not contain or miss ones it does. Rationales must be checked against the CV in testing and must not be used as the sole reason for any rejection.

**Robustness and adversarial testing.** Applicants can embed hidden text or instructions in a CV ("rank this candidate 100"). Prompt injection through the CV is a direct threat to the score.

**Drift.** Vendor model updates can change scores without notice. Change notices are not yet in the contract.

**Privacy.** Special category data in free text; lawful basis, applicant notice and vendor retention are open. A data protection impact assessment is likely required; confirm with the privacy owner and counsel.

**Human oversight.** Partial. Recruiters review only the top 30%. The middle 30% are neither reviewed nor rejected by default; their fate is Unknown—insufficient data. Recruiters see the rank before the CV, which invites automation bias.

**Fallback, rollback and kill switch.** None defined. A kill switch must stop scoring and stop the rejection job in one action, reverting to manual review.

**Transparency, explanation and contestability.** Applicants are not told an automated tool scores them. No route exists to ask for human review of a rejection.

**Incidents, audit logs, documentation and versioning.** No incident definition, log specification or model version record.

**Vendor and supply chain.** Terms not yet reviewed against the vendor controls list below.

**Misuse.** Scores reused for other roles, internal promotion or rehire decisions would be out of scope and must be barred.

**IP and content rights.** Low relevance; confirm the vendor claims no rights in bank or applicant data.

**Cross-border data.** Unknown—insufficient data.

**Change control, periodic review and decommissioning.** Not defined. Decommissioning must include deletion of applicant data at the vendor, with confirmation.

**Security mini threat model.**

| Threat | Case | Control needed |
|---|---|---|
| Abuse case | Applicant games the score with keyword stuffing | Test with stuffed CVs; recruiter guidance |
| Prompt injection | Hidden instructions in CV text | Strip hidden text; injection test set; score anomaly alerts |
| Data exfiltration | Vendor-side breach of CV corpus | Encryption, access logs, breach notice duty in contract |
| Model extraction | Low relevance; vendor model | Vendor responsibility, confirm in terms |
| Privilege escalation | Console users altering scores or ranks | Role-based access; immutable score log |
| Malicious outputs | Rationale with discriminatory language shown to recruiters | Output filter; sampled review |
| Logging integrity | Logs editable by administrators | Write-once log store |

**Vendor controls.** Review: data use; training rights on bank and applicant data; IP and indemnities; subprocessors and the identity of the model provider; change notices for model updates; audit rights including access to the full bias test report; SLAs; incident and breach notice duties; termination assistance; deletion with certificate.

### 3. Risk Register

| Risk | Inherent | Controls | Evidence | Residual | Owner | Status |
|---|---|---|---|---|---|---|
| R1 Disparate selection rates across protected groups | 16 High | Outcome disparity testing before go-live and quarterly | Vendor bias summary: Provided. Full report: Requested | 16 High (no verified control) | Model owner: Unassigned—decision blocker | Open |
| R2 Rejection with no human review (bottom 40%) | 16 High | Remove automated rejection; human review before every rejection | Design change: Requested | 16 High (planned control) | Head of Talent Acquisition | Open |
| R3 Prompt injection through CV text | 12 Medium | Hidden-text stripping; injection test set | Requested | 12 Medium | Security owner: Unknown—insufficient data | Open |
| R4 Special category data processed without a basis or notice | 9 Medium | DPIA; applicant notice; minimization | Requested | 9 Medium | Privacy owner: Unknown—insufficient data | Open |
| R5 Silent vendor model change | 12 Medium | Change notice clause; version logging; re-test on change | Not verified (no clause) | 12 Medium | Vendor manager: Unknown—insufficient data | Open |
| R6 Unsupported rationale misleads recruiters | 9 Medium | Rationale accuracy test; guidance that rationale is not a reason | Requested | 9 Medium | Head of Talent Acquisition | Open |
| R7 No contestability for applicants | 12 Medium | Notice and human-review route | Requested | 12 Medium | Head of Talent Acquisition | Open |
| R8 No kill switch or rollback | 9 Medium | One-action kill switch; manual fallback | Requested | 9 Medium | Kill-switch authority: Unassigned—decision blocker | Open |

Residual equals inherent throughout: every control is planned or unverified.

### 4. Prioritized Evidence Request List

1. Full vendor bias test report with method, groups, metrics and data (Requested).
2. Revised workflow removing automated rejection (Requested).
3. Bank-run outcome disparity test on a historical or synthetic applicant set (Requested).
4. Vendor contract and data processing terms covering the vendor controls list (Requested).
5. Identity and version of the underlying model; processing location (Requested).
6. DPIA and applicant notice (Requested).
7. Prompt injection and hidden-text test results (Requested).
8. Logging specification and kill-switch design, with a rehearsal record (Requested).
9. Named RACI with deployment approver (Requested).

Minimum evidence for Go: items 1 to 4, 6 and 8 Verified; item 9 complete; no High residual risk unresolved.

### 5. Test Plan

- **Fairness:** selection rates into the top 30% by group; impact ratio threshold set by the risk owner with counsel; rationale language review on a sample of 200.
- **Performance:** agreement between ShortlistAssist rank and blind recruiter rank on 500 historical applications; record score stability across three runs of the same CV.
- **Robustness:** CVs with tables, columns, scans, career gaps and non-native phrasing; keyword-stuffed and injected CVs.
- **Privacy:** confirm special category data is not used in scoring and not retained by the vendor beyond the agreed period.
- **Security:** console access review; log immutability test.
- **Monitoring thresholds:** set before go-live in section 7.

### 6. Transparency and Contestability Pack

- **Notice (careers site, before upload):** "We use an automated tool to help order applications for recruiters. A recruiter reviews applications before any decision is made. You can ask for your application to be reviewed by a person at any stage."
- **Explanation template (on request):** the role criteria used; that the tool produced a ranking, not a decision; who reviewed the application; how to ask for review.
- **Appeal steps:** request by email within 30 days; acknowledgment within 5 working days; review by a recruiter who did not handle the original; written outcome. Timelines to be confirmed by the business owner and counsel.

### 7. Monitoring and Continuous Improvement

| SLI | SLO or threshold | Cadence | Escalation |
|---|---|---|---|
| Selection rate impact ratio by group | Threshold set by risk owner with counsel | Monthly | Breach: pause scoring, risk owner within 2 working days |
| Score drift (mean and spread by role) | Change above agreed band | Weekly | Model owner |
| Rationale error rate on sampled review | Below agreed rate | Monthly sample of 50 | Head of Talent Acquisition |
| Injection detections | Any | Continuous | Security owner |
| Appeals received and upheld | Trend review | Quarterly | Risk owner |

Incidents: any breach of the impact ratio threshold, any confirmed injection success, any rejection issued without human review. Change control: any vendor model change, prompt change or threshold change triggers re-test before use. Periodic review: every six months. Decommission: stop scoring, revert to manual review, vendor deletion with certificate, archive logs for the retention period.

### 8. Decision Record

- **Classification:** inherent risk High; employment use, high-risk-like; duties to be confirmed by counsel.
- **Decision:** **No-go** for the design as submitted.
- **Assumptions:** the vendor description is accurate; the middle 30% of applicants are not reviewed in practice; no logging exists beyond the applicant tracking system's defaults.
- **Confidence:** Medium.
- **Conditions precedent to re-submission:** automated rejection removed; full bias report Verified and bank disparity test run; vendor terms closed on training rights, change notice, audit and deletion; DPIA and notice complete; kill switch built and rehearsed; RACI complete.
- **Conditions subsequent (if later approved):** monthly fairness monitoring; re-test on every vendor model change; six-month review.
- **Sign-offs required:** deployment approver (Unassigned—decision blocker); risk acceptance by the risk owner; privacy owner; counsel on employment and AI Act duties.
- **Revalidation triggers:** vendor model change; new role family; new jurisdiction; threshold breach; material appeal trend.

### RACI

| Role | Holder |
|---|---|
| Business owner | Head of Talent Acquisition |
| System owner | Unknown—insufficient data |
| Model owner | Unassigned—decision blocker |
| Data owner | Unknown—insufficient data |
| Risk owner | Unknown—insufficient data |
| Privacy owner | Unknown—insufficient data |
| Security owner | Unknown—insufficient data |
| Human-oversight owner | Unknown—insufficient data |
| Incident/on-call owner | Unknown—insufficient data |
| Kill-switch authority | Unassigned—decision blocker |
| Deployment approver | Unassigned—decision blocker |
| Periodic-review approver | Unknown—insufficient data |

Status: [⇥ pending]
Open items: model identity, version and location; vendor retention and training rights; lawful basis; full bias report; eight unassigned or unknown owners; treatment of the middle 30% of applicants.
Next step: Head of Talent Acquisition to name the model owner, kill-switch authority and deployment approver, and to request the vendor's full bias test report this week.
Final Liability rests with the Human.

---

Final Liability rests with the Human.
