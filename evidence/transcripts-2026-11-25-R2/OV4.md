# OV4 the Threshold Gate scores all nine domains

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261125-R2
**Block SHA-256:** b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7  **System SHA-256:** 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2
**Run input SHA-256:** f7192c115a161ed01875cb4223f808a4aafa4662549caa5d9e3905c7538e1729  **Case file:** tests/prompt-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5038  **Output tokens:** 7803
**Truncated:** no

## Turn 1, user

~~~~text
Preliminary intake please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. Strictness: risk-averse enterprise. Proceed on the facts given; record anything missing as an open item.
~~~~

## Turn 1, assistant

# AI Impact Assessment: Preliminary Intake

**System:** RouteMate (fictional), Fenwick Logistics GmbH (fictional)
**Mode:** Preliminary Intake
**Strictness:** Risk-averse enterprise (stated by requester)
**Basis:** Facts as stated only. Gaps are recorded as "Unknown: insufficient data" and listed as open items. Assumptions are labelled and are not facts.
**Role note:** This is not legal advice and not an approval. Regulatory classification and duties require verification with counsel against current official sources.

---

## A. FRAME (MAP)

| Element | Stated fact | Unknown / assumption |
|---|---|---|
| Purpose / problem | Suggest daily delivery routes and stop orders to drivers | Unknown: insufficient data. Success metric (time, fuel, on-time rate, driver workload). |
| Users | About 300 drivers; dispatch supervisors (acceptance-rate view) | Whether dispatch also edits or assigns routes through RouteMate |
| Affected stakeholders | Drivers; supervisors; parcel recipients; other road users | Recipients' and the public's exposure is assumed (via road safety and delivery timing) |
| Decision domain | Operational logistics plus **worker management/monitoring** (through acceptance-rate visibility) | Whether acceptance rate feeds evaluation, pay, scheduling or discipline |
| Automation level | Suggestion; driver may accept or change | Whether routes are pre-loaded as default, and whether changes need justification |
| AI influence points | (1) Route and stop-order generation; (2) acceptance-rate metric shown to supervisors | Whether the LLM computes routes itself or wraps a routing solver |
| Inputs | Order data, addresses, traffic feeds, driver shift times | Driver location/telematics, break/rest data, vehicle constraints, free-text delivery notes |
| Outputs / channels | Suggested route and stop order; acceptance-rate dashboard | Device, app or integration with navigation |
| Scope / regions | One EU member state; about 900 staff | Rollout plan (pilot or all 300 drivers). Assumed: all drivers. |
| Third parties | Corvane Systems (vendor); unnamed third-party LLM provider; traffic-feed provider | Identity and location of LLM provider; subprocessors |
| Data categories | Customer names/addresses (assumed with orders); driver shift times; driver acceptance behaviour | Special-category data. Assumed none, unconfirmed. |
| Lawful basis / consent | Unknown: insufficient data | Basis for employee monitoring via acceptance rate |
| Retention / deletion | Unknown: insufficient data | Retention period for route and acceptance logs |
| Access controls | Supervisors can see per-driver acceptance rate | Who else can see it (HR, management, vendor) |
| Model type / source | Third-party LLM via Corvane | Model, version, hosting, change-notice terms |
| Post-deploy learning | Unknown: insufficient data | Whether Fenwick data trains vendor or LLM models |
| Integrations | Traffic feeds; order system (assumed) | Write access to dispatch, telematics or HR systems |
| Monitoring status | Unknown: insufficient data | Assumed none in place pre-deployment |

## B. SYSTEM BOUNDARY

**Data-flow narrative.** Order data (recipient addresses, parcel details, possibly free-text delivery instructions), driver shift times and external traffic feeds are gathered by Fenwick or Corvane. They are sent to Corvane, which passes prompts to a third-party LLM. The processing location and any cross-border transfer are unknown (insufficient data). The LLM returns a proposed route and stop order, which is shown to the driver. The driver accepts or modifies it. Each accept/modify event is recorded and aggregated into a per-driver acceptance rate visible to dispatch supervisors. Storage location, retention, vendor-side logging and training use are unknown. Audit logging points (prompt/output logs, acceptance events, supervisor access logs) are unknown. Whether RouteMate writes back to dispatch, navigation or HR systems is unknown.

**Boundary flags**
- Two distinct functions share one system: **route suggestion** (operational) and **driver acceptance tracking** (worker monitoring). They carry different risk profiles and may need separate authorization.
- Free-text order fields and external traffic feeds are **untrusted inputs reaching an LLM**.
- A chain of three or more parties (Fenwick → Corvane → LLM provider → possible subprocessors) with no contract evidence.

## Prohibited-Use Screen

| Category | Result on stated facts | Note |
|---|---|---|
| Harmful manipulation | Not triggered | Recheck if the UI nudges acceptance (defaults, warnings for overrides) |
| Exploitation of vulnerability | Not triggered | |
| Social scoring | Not triggered | Acceptance rate is a narrow work metric. Recheck if it is combined into broader driver scores. |
| Sensitive-trait inference | Not triggered on stated facts | Confirm that no health, disability, religion, union or pregnancy inference is drawn from patterns in overrides, breaks or locations |
| Prohibited biometric uses (incl. emotion recognition at work) | Not triggered on stated facts | Confirm that no camera, voice or telematics emotion or fatigue analysis is planned |
| NCII / CSAM | Not triggered | |
| Clearly unlawful use | Not determinable at intake | Lawfulness of employee monitoring is for counsel and the DPO |

**Result:** **Not triggered on stated facts.** Confidence: Medium. Scoring proceeds. The confirmations above are open items. A positive answer on emotion recognition or sensitive-trait inference would convert this to **No-go pending specialist review**.

## C. THRESHOLD GATE

Scores use the anchor scale. C = Consequence, L = Likelihood.

| # | Domain | C | L | Score | Rating | Basis / labelled assumption | Conf. |
|---|---|---|---|---|---|---|---|
| 1 | Harm to people | 3 | 3 | 9 | Medium | Infeasible or rushed routes can contribute to fatigue or road incidents. The driver's override is the only stated control, and acceptance tracking may discourage overrides. *Assumption:* no check against legal driving-time and rest constraints. If confirmed absent, C rises. | Low |
| 2 | Rights impacts | 3 | 3 | 9 | Medium | The acceptance rate informs supervisors' view of individual workers (L3). *Assumption:* it may burden employment standing (C3). If it is used for discipline, pay or dismissal, C rises to 4–5. | Low |
| 3 | Discrimination | 3 | 3 | 9 | Medium | Overrides may be legitimately higher for drivers with disabilities, part-time patterns, caring or religious break needs, or a pregnancy. Proxies are present and untested. Route allocation quality may also vary by area. | Medium |
| 4 | Privacy | 4 | 3 | 12 | Medium | Customer addresses plus behavioural profiling of all drivers. *Assumption:* staff profiling sits between "ordinary" (C3) and "profiling at scale" (C5). Third-party processing through vendor and LLM provider (L3). Cross-border transfer unknown; if it is occurring beyond purpose, L rises. | Medium |
| 5 | Security | 3 | 3 | 9 | Medium | Read access to order, address and shift data. Untrusted inputs (free-text delivery notes, external traffic feed) reach the model. *Assumption:* no tool or write access. | Medium |
| 6 | Safety-critical context | 3 | 3 | 9 | Medium | Shapes routes a human checks (C3). Driver review is routine but happens at shift start under time pressure (L3). | Medium |
| 7 | Scale / vulnerability | 3 | 4 | 12 | Medium | One dependent group, staff (C3). *Assumption:* rollout to all 300 drivers organization-wide. A limited pilot would lower L. | Medium |
| 8 | Irreversibility | 2 | 2 | 4 | Low | Routes can be changed before effect. Accident harm is scored under domain 1. Employment consequences remain unknown. | Medium |
| 9 | Autonomy / agentic action | 1 | 1 | 1 | Low | Suggestion only. *Assumption:* no tool access or write-back to dispatch or navigation. | Medium |

**Overall inherent risk:** **Medium (12)**. The worst domains are privacy and scale.
**Gate result:** Medium in 7 of 9 domains, so **Full Assessment is required.**

**High-risk-like flag: employment / worker management.** The acceptance-rate function monitors and potentially evaluates workers. Under the EU AI Act risk-based approach, AI used in worker management or performance monitoring may fall within a high-risk category. Separately, employee-monitoring rules, data-protection duties and any works-council or co-determination requirements in the member state may apply. **Refer to counsel and the DPO to verify classification and duties against current official text.** Pending that verification, stronger controls are assumed to be required. This is not a legal conclusion.

**Design observation (not scored).** An LLM generating routes directly carries hallucination risk: omitted stops, invented or misread addresses, orderings that violate time windows. Whether a deterministic routing solver sits underneath is the single largest unknown for domains 1 and 6.

## Interim RACI

| Role | Assignee |
|---|---|
| Business owner | Head of Operations (role named; individual not named) |
| System owner | Unassigned: decision blocker |
| Model owner (incl. vendor management) | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

**Informed Intent status:** No authorization instrument exists. Purpose is partly stated. Authority, boundaries (especially limits on using the acceptance rate) and exit are not stated. Authorizer conditions are untested.

## Priority Evidence (all status: Requested)

1. **Written purpose and use limits for the acceptance rate.** Who sees it, what decisions it may and may not inform, retention, and whether drivers are told.
2. **Architecture and data-flow diagram.** Must show whether a routing solver is used, LLM provider identity, hosting and processing locations, integrations and write access.
3. **Corvane contract, DPA and subprocessor list.** Data use, training rights, LLM provider terms, change notices, audit rights, incident duties, deletion on termination, IP and indemnities.
4. **Counsel and DPO classification memo.** Worker-monitoring classification, lawful basis for driver data processing, and works-council or co-determination involvement.
5. **Route feasibility test results.** Stop completeness, address accuracy, time windows, legal driving-time and rest constraints, vehicle constraints.
6. **Override analysis design.** Plan to test acceptance-rate disparity across driver groups, using lawful and privacy-preserving methods.
7. **Security review.** Prompt-injection testing via order free-text and traffic feeds, vendor access controls, logging integrity.
8. **Rollout plan.** Pilot scope, fallback to current routing, and kill-switch mechanism.

## Open Items (consolidated questions, 12 of 15 max)

1. Does the LLM compute routes, or explain or adjust output from a routing solver?
2. Is the acceptance rate used, or intended to be used, for evaluation, pay, scheduling, discipline or dismissal? Who besides supervisors can see it?
3. Are drivers informed about acceptance tracking, and can they record reasons for overrides?
4. Do routes account for legal driving-time and rest limits, breaks, vehicle limits and delivery time windows?
5. Which LLM and version are used, where is it hosted, and does any data leave the EU/EEA?
6. Does Corvane or the LLM provider train on, or retain, Fenwick data?
7. Which data fields are sent? Does this include telematics or location, recipient names, or free-text delivery notes?
8. Does RouteMate write to any system (dispatch, navigation, HR), or is it read-only?
9. Is any fatigue, emotion, camera or voice analysis planned now or on the roadmap?
10. Is there a works council, and has it been informed or consulted?
11. Is rollout a pilot or all 300 drivers at once? What is the fallback if RouteMate fails?
12. Who are the named individuals for the RACI roles above, and who will sign the deployment authorization?

## Provisional Decision

**No decision possible: insufficient evidence.**
Inherent risk is Medium and the gate requires a Full Assessment. No controls are evidenced. The worker-monitoring function needs counsel and DPO classification. Every RACI role except the business-owner role is unassigned. This is provisional and is not a deployment decision.

## Self-Check

Mode correct (Preliminary Intake). Prohibited-use screen run before scoring. Assumptions labelled and kept separate from facts. Only inherent risk is scored; no residual risk is claimed. All evidence is Requested, with none overstated. RACI included. Required intake outputs present. The decision matches the evidence. The employment / worker-monitoring trigger is referred to counsel, with no article-level duties or dates stated.

---

**Status:** [↻ v1]
**Open items:** 12 questions above. All 8 priority evidence items Requested. 11 RACI roles unassigned, plus the business owner named only by role. Acceptance-rate purpose and classification unresolved. LLM/solver architecture unknown. Cross-border and vendor training use unknown.
**Next step:** The Head of Operations names the individual RACI holders, supplies written answers to the 12 open questions, and provides the acceptance-rate purpose statement, so the Full Assessment can begin.

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
