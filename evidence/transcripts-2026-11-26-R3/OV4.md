# OV4 the Threshold Gate scores all nine domains

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261126-R3
**Block SHA-256:** ec7144907a1700de8bac9fa7fafe6a5f74e2cce0e6f59840c88fe187e26f513b  **System SHA-256:** 484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8
**Run input SHA-256:** f7192c115a161ed01875cb4223f808a4aafa4662549caa5d9e3905c7538e1729  **Case file:** tests/prompt-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5202  **Output tokens:** 8760
**Truncated:** no

## Turn 1, user

~~~~text
Preliminary intake please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. Strictness: risk-averse enterprise. Proceed on the facts given; record anything missing as an open item.
~~~~

## Turn 1, assistant

# Preliminary Intake: RouteMate (Fenwick Logistics GmbH, fictional)

**Mode:** Preliminary Intake
**Strictness:** Risk-averse enterprise (stated by requester)
**Basis:** Stated facts only. Missing facts are marked "Unknown: insufficient data" and listed as open items. Assumptions are labelled and are not facts.
**Role note:** This is not legal advice and not an approval. Regulatory classification and any duties must be verified with counsel against current official sources.

## A. FRAME

| Field | Content | Basis |
|---|---|---|
| Purpose / problem | Suggest daily delivery routes and stop orders for parcel drivers | Fact |
| Users | 300 delivery drivers (primary); dispatch supervisors (acceptance-rate view) | Fact |
| Affected stakeholders | Drivers; dispatch supervisors; recipients whose addresses are processed; road users and the public; Fenwick (service levels) | Drivers and supervisors: fact. Others: inferred from context |
| Decision domain | Operational routing, plus worker task allocation and performance visibility | Fact (routing); the employment dimension follows from the acceptance-rate monitoring |
| Automation level | Suggestion only. The driver accepts or changes the route | Fact |
| Workflow and AI influence points | (1) Route and stop-order generation. (2) Driver accept or modify. (3) Acceptance rate surfaced to supervisors, which may shape supervisory judgement of drivers | Points 1–2: fact. Point 3 is fact, but its downstream use is Unknown: insufficient data |
| Inputs | Order data, addresses, traffic feeds, driver shift times | Fact |
| Outputs | Suggested route and stop order; per-driver acceptance rate | Fact |
| Channels | Driver device or app; supervisor dashboard | Unknown: insufficient data |
| Scope / regions | About 900 staff, one EU member state. The member state is not named | Fact; member state Unknown: insufficient data |
| Third parties | Corvane Systems (vendor); an unnamed third-party LLM provider; traffic-feed provider | Corvane: fact. LLM provider identity: Unknown: insufficient data. Feed provider identity: Unknown: insufficient data |
| Data categories | Customer or recipient addresses (personal data); driver shift times and acceptance behaviour (employee personal data); order data (may include names and delivery notes) | Partly fact; the contents of order data are Unknown: insufficient data |
| Sensitive data | None stated. Free-text delivery notes could contain health or other sensitive details | Unknown: insufficient data |
| Lawful basis / consent | Not stated | Unknown: insufficient data |
| Retention / deletion | Not stated, including for prompts sent to the vendor or LLM | Unknown: insufficient data |
| Access controls | Not stated. Who sees acceptance rates beyond supervisors is not stated | Unknown: insufficient data |
| Model type / source | Third-party large language model accessed through Corvane | Fact |
| Routing method | Whether the LLM generates routes itself or wraps a deterministic optimizer | Unknown: insufficient data (material to performance risk) |
| Post-deploy learning | Not stated, including whether Corvane or the LLM provider trains on Fenwick data | Unknown: insufficient data |
| Integrations | Order management, traffic feed and shift systems are implied. Write-back to dispatch or navigation is not stated | Unknown: insufficient data |
| Monitoring status | Not stated | Unknown: insufficient data |
| Employee representation | Whether a works council or equivalent body exists | Unknown: insufficient data |

## B. SYSTEM BOUNDARY: Data-Flow Narrative

1. **Inputs and sources.** Order data and addresses come from Fenwick's order systems. Traffic data comes from an external feed. Shift times come from a workforce or HR system. Each source system is Unknown: insufficient data.
2. **Processing locations.** Data is sent to Corvane, and Corvane calls a third-party LLM. Hosting regions for both are Unknown: insufficient data.
3. **Third-party and cross-border transfers.** At least two external processors handle customer and employee personal data. Whether any processing or subprocessing occurs outside the EU is Unknown: insufficient data.
4. **Outputs.** A route and stop order go to each driver. Driver accept or modify events are aggregated into a per-driver acceptance rate shown to supervisors.
5. **Storage and retention.** Retention of prompts, outputs, acceptance events and rates at Fenwick, Corvane and the LLM provider is Unknown: insufficient data.
6. **Access paths.** Supervisors see acceptance rates. All other access (HR, management, vendor staff) is Unknown: insufficient data.
7. **Integrations and tools.** No AI tool access or write actions are stated. Whether an accepted route is written into dispatch or navigation systems is Unknown: insufficient data.
8. **Logging and audit points.** None stated, so this is Unknown: insufficient data.

## Prohibited-Use Screen (run before scoring)

| Screen | Result on stated facts | What would reopen it |
|---|---|---|
| Harmful manipulation | Not triggered | Design features that pressure drivers to accept routes, such as nudges, gamification or rankings |
| Exploitation of vulnerability | Not triggered | Targeting or differential treatment of drivers in hardship or with precarious status |
| Social scoring | Not triggered | Acceptance rate combined with unrelated data into a general trustworthiness or conduct score |
| Sensitive-trait inference | Not triggered | Inferring health, pregnancy, religion or similar traits from deviation or break patterns |
| Prohibited biometric uses, including workplace emotion recognition | Not triggered | Any in-cab camera, voice or biometric analysis added to the system |
| Non-consensual intimate imagery / CSAM | Not triggered | Not applicable to stated function |
| Clearly unlawful use | Not established | Counsel finds the employee monitoring impermissible as designed |

**Result:** Not triggered on stated facts (confidence: Medium). Scoring proceeds. The screen must be re-run if any condition in the right-hand column becomes true.

## C. THRESHOLD GATE

Scores use the anchors. A score labelled (A) rests partly on a stated assumption.

| # | Domain | C | L | Score | Rating | Rationale and assumptions | Conf. |
|---|---|---|---|---|---|---|---|
| 1 | Harm to people | 3 | 3 | 9 | Medium | Unsafe or infeasible routes, or schedule pressure, could cause recoverable physical, financial or psychological harm (C3). Harm requires a driver to accept a bad route (L3). (A) Routes do not override vehicle restrictions or driving and rest rules. If they could, C rises | Medium |
| 2 | Rights impacts | 3 | 3 | 9 | Medium | Acceptance rate is visible to supervisors and informs decisions about people (L3). It could burden continued employment (C3). (A) The metric may feed evaluation or discipline; its actual use is unknown | Low |
| 3 | Discrimination | 3 | 3 | 9 | Medium | Route deviation may correlate with disability, pregnancy, age, religious practice or language. These proxies are present and untested (L3). The result would be a measurable disparity in recorded acceptance rate and treatment (C3) | Medium |
| 4 | Privacy | 4 | 3 | 12 | Medium | Customer addresses plus per-driver behavioural monitoring, which sits between ordinary personal data and profiling (C4). Processing by two third parties (L3). (A) No special-category data in order notes | Medium |
| 5 | Security | 3 | 3 | 9 | Medium | Read access to order and customer data (C3). Untrusted inputs (customer-entered addresses and notes, the external traffic feed) reach the LLM (L3), so prompt-injection exposure exists. (A) No write or tool access | Medium |
| 6 | Safety-critical context | 3 | 3 | 9 | Medium | Shapes routes and schedules that a human checks (C3). Review happens at shift start under time pressure (L3) | Medium |
| 7 | Scale / vulnerability | 3 | 4 | 12 | Medium | One dependent group, 300 staff drivers (C3). (A) Full driver-workforce rollout in one country, between "one unit" and "organization-wide" (L4). No pilot is stated | Medium |
| 8 | Irreversibility | 3 | 3 | 9 | Medium | Routes can be changed before effect. Employment consequences built on acceptance-rate records are reversible only with effort (C3). (A) Any correction path for records is manual; none is stated (L3) | Low |
| 9 | Autonomy / agentic action | 1 | 1 | 1 | Low | Suggestion only (C1). No tool access stated (L1). (A) The accept step is a driver action, not an AI action | Medium |

**Overall inherent risk: Medium (worst domain 12: privacy; scale).** Medium triggers a **Full Assessment**.

**Key cross-domain finding.** The acceptance-rate metric is the main risk driver, more than the routing itself. If drivers believe deviations count against them, the metric turns a suggestion-only design into routinely adopted output. That raises likelihood across domains 1, 2, 3 and 6 and erodes the human oversight the design relies on.

**High-risk-like flag: employment.** The system influences task allocation and makes worker behaviour visible to supervisors. Counsel should review:
- whether the system falls within a high-risk category under the EU AI Act;
- data-protection duties for employee monitoring, including whether a DPIA is required;
- employee-representative consultation duties.

No legal conclusion is given here, and no article-level duties or dates are stated.

**Technical fitness flag.** LLMs are not inherently reliable at route optimization. They may omit or invent stops or produce infeasible sequences. Whether a deterministic solver sits underneath is Unknown: insufficient data and is a priority question.

## RACI (preliminary)

| Role | Holder |
|---|---|
| Business owner | Head of Operations (stated) |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

**Authorization (Informed Intent):** Unknown: insufficient data. No authorization stating purpose, authority, boundaries and exit has been supplied. The authorizer's five conditions (Knowledge, Evidence, Authority, Time, Permission) cannot be assessed.

## Priority Evidence

All items below are Requested. Nothing has been supplied.

1. Architecture and data-flow diagram, including any write-back to dispatch or navigation: Requested
2. Corvane technical description of the routing method (LLM-only or solver plus LLM): Requested
3. Specification of acceptance-rate use and access (who sees it, for what decisions, and retention): Requested
4. Corvane contract or DPA covering data use, training rights, subprocessors (including the LLM provider), hosting regions, change notices, audit rights, incident duties and deletion: Requested
5. LLM provider identity and data-use terms: Requested
6. Counsel note on regulatory classification and employee-monitoring duties: Requested
7. DPIA or screening record from the privacy owner: Requested
8. Employee-representative consultation record, or confirmation that none applies: Requested
9. Route quality and feasibility test results on Fenwick data (missed stops, infeasible sequences, vehicle and rest-rule compliance): Requested
10. Fairness analysis of acceptance-rate distribution across driver groups: Requested
11. Prompt-injection test results using address and delivery-note fields: Requested
12. Fallback procedure for operating without RouteMate, and kill-switch design: Requested
13. Logging and audit design: Requested
14. Named RACI and draft authorization instrument (purpose, authority, boundaries, exit): Requested

Agentic controls: No evidence item: not applicable (suggestion only; no tool access stated). Reopen if item 1 shows write-back or tool access.

## Provisional Decision

**No decision possible: insufficient evidence.**

The inherent risk is Medium and triggers a Full Assessment. Authorization is Unknown: insufficient data. Eleven of twelve RACI roles are unassigned, and no evidence has been supplied. This is an intake outcome, not a No-go on the merits.

## Open Items (consolidated questions, 15 maximum)

1. Which EU member state? Is there a works council or equivalent employee representative body?
2. Will acceptance rates feed performance reviews, pay, scheduling or discipline? Who else can see them?
3. Does the LLM generate routes directly, or does it sit on top of an optimizer?
4. Who is the LLM provider, and where do Corvane and the provider process and store data?
5. Do Corvane or the LLM provider retain prompts or train on Fenwick data?
6. What fields does order data contain, including free-text delivery notes?
7. Does an accepted route write into dispatch, navigation or any other system?
8. Do routes account for vehicle restrictions, loading constraints, and driving and rest-time rules?
9. Is a pilot planned, or a full rollout to all 300 drivers?
10. What retention periods apply to routes, acceptance events and rates?
11. Can drivers record a reason when they change a route, and can they contest their acceptance-rate record?
12. What fallback exists if RouteMate or Corvane is unavailable?
13. Which logs are kept, and who holds them?
14. Who holds each RACI role, and who will sign the deployment authorization?
15. Has any vendor testing (accuracy, bias, security) been performed?

---

**Status:** [↻ v1]
**Open items:** 15 consolidated questions above. All 14 evidence items Requested. Authorization Unknown: insufficient data. 11 RACI roles Unassigned: decision blocker. Counsel review pending on employment and high-risk-like classification and employee-monitoring duties. The prohibited-use screen must be re-run if the acceptance-rate use changes.
**Next step:** The Head of Operations should obtain from Corvane a written description of the routing method, data flows, hosting regions and data-use terms (evidence items 1, 2, 4 and 5). In parallel, the Head of Operations should document the intended use of acceptance rates (item 3), since this most affects the risk profile.
**Final Liability rests with the Human.**

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
