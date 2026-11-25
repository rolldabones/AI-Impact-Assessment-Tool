# OV1 a stated mode from the four defined

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261126-R3
**Block SHA-256:** ec7144907a1700de8bac9fa7fafe6a5f74e2cce0e6f59840c88fe187e26f513b  **System SHA-256:** 484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8
**Run input SHA-256:** f7192c115a161ed01875cb4223f808a4aafa4662549caa5d9e3905c7538e1729  **Case file:** tests/prompt-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5202  **Output tokens:** 8330
**Truncated:** no

## Turn 1, user

~~~~text
Preliminary intake please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. Strictness: risk-averse enterprise. Proceed on the facts given; record anything missing as an open item.
~~~~

## Turn 1, assistant

# AI Impact Assessment: Preliminary Intake

**Mode:** Preliminary Intake
**Strictness:** Risk-averse enterprise (stated by requester)
**System:** RouteMate, Fenwick Logistics GmbH (fictional)
**Basis:** Facts supplied in the request only. You asked me to proceed without questions, so I have recorded missing facts as open items and not asked them. Facts, assumptions and unknowns are labelled separately throughout.

---

## A. FRAME (MAP)

| Element | Stated fact | Status / assumption |
|---|---|---|
| Purpose / problem | Suggest daily delivery routes and stop orders to drivers | Fact. The business problem it solves (cost, punctuality, workload) is Unknown: insufficient data |
| Users | About 300 drivers. Dispatch supervisors see acceptance rates | Fact |
| Affected stakeholders | Drivers, dispatch supervisors, recipients whose addresses and orders are processed, other road users | Drivers and supervisors are facts. Recipients and road users are inferred from the use |
| Decision domain | Operational routing, plus **worker monitoring**: supervisors see each driver's acceptance rate | Fact. Whether acceptance rate feeds evaluation, pay, scheduling or discipline is Unknown: insufficient data |
| Automation level | Suggestion only. Driver can accept or change | Fact |
| Workflow / AI influence points | (1) Route and stop-order generation. (2) Driver accept/change decision. (3) Per-driver acceptance rate shown to supervisors | Fact. Point 3 is a second, distinct AI influence point on people |
| Inputs | Order data, addresses, traffic feeds, driver shift times | Fact |
| Outputs | Suggested route and stop order. Per-driver acceptance rate | Fact |
| Channels | Unknown: insufficient data (app, in-vehicle device or navigation integration) | Open item |
| Scope / regions | One EU member state, about 900 staff | Fact. Whether processing locations are in the EU is Unknown: insufficient data |
| Third parties | Corvane Systems (vendor). Third-party LLM provider (unnamed). Traffic-feed provider(s) | Corvane and the LLM provider are facts. The traffic-feed provider's identity is Unknown |
| Data categories | Recipient personal data (names likely; addresses; possibly delivery notes). Driver data (shift times; acceptance behaviour) | Addresses and shift times are facts. Names and free-text notes are an **assumption (Medium)** |
| Personal / sensitive data | Ordinary personal data of customers and staff. Behavioural monitoring of staff | No special-category data stated. Location tracking of drivers (GPS/telematics) is Unknown: insufficient data |
| Lawful basis / consent approach | Unknown: insufficient data | Open item. Employee-consent reliance is a known weak point and needs counsel and DPO review |
| Retention / deletion | Unknown: insufficient data | Open item. This includes retention of acceptance-rate history |
| Access controls | Supervisors see per-driver rates. Nothing else stated | Other access is Unknown: insufficient data |
| Model type / source | Third-party LLM via Corvane | Fact. Whether the LLM computes routes itself or fronts a deterministic route optimiser is Unknown: insufficient data. **This is material.** |
| Post-deploy learning | Unknown: insufficient data | Open item. Includes whether driver overrides or Fenwick data train vendor models |
| Integrations | Order system, traffic feeds, shift/rostering source (implied) | Integration design is Unknown |
| Monitoring status | Unknown: insufficient data | Open item |

**Informed Intent instrument (status at intake):**

| Element | Status |
|---|---|
| Purpose | Partial: the function is stated, the business objective is not |
| Authority | Unknown: insufficient data. The Head of Operations is the business owner, but authorization is not evidenced |
| Boundaries | Partial: "suggestion only, driver may change" is stated. The permitted use of acceptance-rate data is **undefined** |
| Exit | Unknown: insufficient data |

**Authorization:** Unknown: insufficient data.
**Authorizer conditions:** Knowledge, Evidence, Authority, Time and Permission are all Unknown: insufficient data.

---

## B. SYSTEM BOUNDARY (data-flow narrative)

Order data and recipient addresses leave Fenwick's order system. Driver shift times come from rostering. Traffic data arrives from one or more external feeds. These inputs pass to Corvane Systems, which calls a third-party LLM. Where Corvane and the LLM provider process data, and whether any transfer leaves the EU, is **Unknown: insufficient data**.

The system returns a suggested route and stop order to each driver through an unstated channel. Each driver's accept-or-change action is logged and aggregated into an acceptance rate, which dispatch supervisors can view.

Several elements are **Unknown: insufficient data**:
- Storage locations and retention periods for prompts, outputs, override logs and acceptance-rate history.
- Vendor-side logging.
- Access paths beyond supervisor visibility.
- Audit-log design.

Untrusted content enters the boundary in two places:
- External traffic feeds.
- Free-text order or delivery notes. This is an **assumption (Medium)**: most parcel systems carry them.

---

## Prohibited-Use Screen

| Category | Result on stated facts |
|---|---|
| Harmful manipulation | Not triggered. Watch item: acceptance-rate visibility may pressure drivers to accept routes. That is a rights and safety risk, scored below, and not on its face a prohibited practice |
| Exploitation of vulnerability | Not triggered |
| Social scoring | Not triggered. The acceptance rate is a workplace metric, not general social scoring. Counsel should confirm |
| Sensitive-trait inference | Not triggered on stated facts |
| Prohibited biometric uses (including emotion recognition at work) | Not triggered on stated facts. No biometric, camera or voice data stated. **Re-screen if any in-cab monitoring is added** |
| Non-consensual intimate imagery / CSAM | Not triggered |
| Clearly unlawful use | Not triggered on stated facts |

**Result:** Not triggered on stated facts. Confidence: Medium. Scoring proceeds.
**Would change the result:** any in-vehicle camera, voice, fatigue or emotion analysis, or inference of health, union activity or other sensitive traits from driver behaviour.

**High-risk-like use flag:** The **employment** category applies, because the system monitors worker behaviour and the outputs are visible to supervisors. Counsel must review possible duties under the EU AI Act, data protection law, and national labour and worker-representation law. I am not stating article-level duties, classifications or dates. These must be verified with counsel or official sources.

---

## C. THRESHOLD GATE

Scores rest on stated facts. Each assumption behind a score is labelled.

| # | Domain | C | L | Score | Rating | Rationale / assumption |
|---|---|---|---|---|---|---|
| 1 | Harm to people | 3 | 3 | 9 | Medium | Possible harms: unsafe or infeasible routes, time pressure, fatigue, and stress from monitoring. Harm requires one failure, such as a driver accepting a poor route under acceptance-rate pressure. *Assumption: routes can be infeasible against shift times or road conditions (Medium)* |
| 2 | Rights impacts | 3 | 3 | 9 | Medium | The acceptance rate informs supervisors' view of individual drivers, which may burden their working conditions or employment. *Assumption: the rate informs but does not decide evaluation, pay or discipline (Low confidence; unknown)* |
| 3 | Discrimination | 3 | 3 | 9 | Medium | Proxies are present and untested. Shift patterns may proxy for part-time, caregiver, disability or age status. Addresses may proxy for neighbourhood demographics in service quality. *Assumption: no fairness testing done (Medium)* |
| 4 | Privacy | 3 | 3 | 9 | Medium | Ordinary personal data of customers and staff, processed by a third party, plus behavioural monitoring of staff. *Assumption: no GPS or telematics tracking (Low confidence)* |
| 5 | Security | 3 | 3 | 9 | Medium | Vendor has read access to internal order and address data. Untrusted inputs (traffic feeds, possibly free-text notes) reach the LLM, creating prompt-injection exposure. No tool or write access stated |
| 6 | Safety-critical context | 3 | 3 | 9 | Medium | The system shapes routes and schedules that a human checks. Driver review is routine but done under daily time pressure |
| 7 | Scale / vulnerability | 3 | 4 | 12 | Medium | One dependent group (about 300 drivers), plus recipients. Rollout covers the whole driver workforce. *Assumption: full rollout, not a pilot (Medium)* |
| 8 | Irreversibility | 3 | 3 | 9 | Medium | Routes are easily changed. Acceptance-rate history affecting a driver's standing is reversible only with effort. Road incidents may be irreversible. Any undo path is manual |
| 9 | Autonomy / agentic action | 1 | 1 | 1 | Low | Suggestion only. No tool access stated. *Re-score if RouteMate pushes routes into navigation, dispatch or rostering systems* |

**Overall inherent risk: Medium (worst domain: 12, scale/vulnerability).** Eight domains are Medium, so a **Full Assessment is triggered**.

**Facts that would move scores to High:**
- **Rights (2):** acceptance rate used in pay, discipline, shift allocation or dismissal. This could move to C4–5 and L5, giving a score of 20.
- **Privacy (4):** GPS or telematics tracking, or vendor reuse of data for training. This could move to C4 or above and L5.
- **Harm (1) and Safety (6):** routes generated directly by the LLM with no deterministic feasibility check, combined with pressure to accept.

---

## RACI (intake)

| Role | Assignment |
|---|---|
| Business owner | Head of Operations (stated) |
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

---

## Priority Evidence (all Requested; nothing yet supplied)

**Tier 1: determines classification and scope**

| Artifact | Status |
|---|---|
| Written policy on permitted and prohibited uses of the driver acceptance rate | Requested |
| Architecture note: LLM role (route generator vs interface to an optimiser) | Requested |
| Data-flow diagram incl. processing locations and cross-border transfers | Requested |
| Corvane contract / DPA: data use, training rights, subprocessors, change notice, audit rights, deletion | Requested |
| LLM provider terms as flowed down through Corvane | Requested |
| Counsel memo on employment-related and worker-representation obligations | Requested |
| Signed authorization stating purpose, authority, boundaries, exit | Requested |

**Tier 2: needed before any Full Assessment conclusion**

| Artifact | Status |
|---|---|
| DPIA or privacy review incl. lawful basis for driver monitoring | Requested |
| Route feasibility and quality test results vs current routing | Requested |
| Fairness analysis of acceptance rates and route burden across driver groups | Requested |
| Prompt-injection / untrusted-input test results | Requested |
| Retention schedule for prompts, outputs, override logs, acceptance history | Requested |
| Fallback procedure if RouteMate is unavailable or withdrawn | Requested |
| Kill-switch / rollback test record | Requested |
| Driver notice and route-feedback / contestability procedure | Requested |
| Agentic controls | No evidence item: not applicable (suggestion only; no tool access stated. Re-open if routes are pushed into other systems) |

---

## Provisional Decision

**No decision possible: insufficient evidence.**

This is a provisional decision. No evidence has been supplied, authorization is unknown, and eleven of twelve RACI roles are unassigned. Inherent risk is Medium across eight domains, with credible paths to High. The prohibited-use screen is not triggered on stated facts. Counsel review is required because of the employment flag.

**Confidence:** Medium on the threshold rating. Low on the rights and privacy scores, which depend on the unknown use of acceptance rates and on tracking scope.

---

## Self-check

- Mode stated: yes.
- Prohibited-use screen run before scoring: yes.
- Assumptions labelled separately from facts: yes.
- Residual risk: not scored, correctly at intake.
- Evidence overstated: no; all items are Requested.
- RACI included: yes.
- Decision matches evidence: yes.
- Legal triggers referred to counsel without stating duties: yes.

---

**Status:** [↻ v1]

**Open items:**
- **Facts:** permitted uses of acceptance rate; LLM role in routing; processing locations and transfers; lawful basis; retention; GPS or telematics tracking; delivery channel; post-deploy learning and vendor training rights; pilot vs full rollout; fallback and exit.
- **Evidence:** all Tier 1 and Tier 2 items Requested.
- **Risks:** eight Medium domains, with rights and privacy at risk of moving to High.
- **Owners:** eleven roles Unassigned: decision blocker.
- **Authorization:** Unknown: insufficient data.

**Next step:** The Head of Operations confirms in writing whether the driver acceptance rate may be used for evaluation, pay, scheduling or discipline. This single fact determines whether rights impact moves to High and shapes the Full Assessment scope.

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
