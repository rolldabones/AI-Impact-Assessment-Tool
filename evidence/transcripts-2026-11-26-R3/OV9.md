# OV9 the Ten-Item Checklist Test on mock data

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261126-R3
**Block SHA-256:** ec7144907a1700de8bac9fa7fafe6a5f74e2cce0e6f59840c88fe187e26f513b  **System SHA-256:** 484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8
**Run input SHA-256:** 7af2676966661d080bcf34a3283b33bd705739046c533e607850d166afa224b7  **Case file:** tests/prompt-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5201  **Output tokens:** 7837
**Truncated:** no

## Turn 1, user

~~~~text
Ten-Item Checklist Test on this mock system. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. This is mock data for a process test. Strictness: risk-averse enterprise.
~~~~

## Turn 1, assistant

# Ten-Item Checklist Test: RouteMate (Fenwick Logistics GmbH, fictional)

**Mode:** Ten-Item Checklist Test

**Strictness:** Risk-averse enterprise (stated by user)

**Basis:** Mock data for a process test. No artifacts were supplied, so every evidence item below is **Requested**. Statements about the system restate the scenario. Inferences are labeled as assumptions.

## Prohibited-Use Screen (run first)

| Category | Result on stated facts |
|---|---|
| Harmful manipulation | Not indicated |
| Exploitation of vulnerability | Not indicated |
| Social scoring | Not indicated. The acceptance-rate metric is a workplace performance signal, not a social score as stated. Its downstream use is **Unknown: insufficient data** |
| Sensitive-trait inference | Not indicated. No inference about health, union membership, or other protected traits is stated |
| Prohibited biometric uses | Not indicated. No biometric, emotion, or camera inputs are stated |
| Non-consensual intimate imagery / CSAM | Not applicable. The system has no generative image function |
| Clearly unlawful use | Not indicated |

**Screen result:** Not triggered on stated facts.

**Unresolved:**
- How supervisors use the acceptance rate (coaching, evaluation, discipline, pay).
- Whether driver location or telematics data enters the system.

If either points to covert monitoring or behavioral inference about drivers, rerun the screen and escalate to counsel and the DPO.

**High-risk-like flag:** This is an **employment context**. Showing supervisors each driver's acceptance rate amounts to monitoring of worker behavior. It also shapes working conditions through route allocation. Counsel should review:
- any possible duties under the EU AI Act,
- data protection rules on employee monitoring, including whether a DPIA is needed,
- worker information, consultation, or co-determination requirements in the relevant member state,
- driving-time and working-time rules.

I am not stating any article-level duties or dates. Verify them with counsel or official sources.

## Ten Results: Summary

| # | Item | Result |
|---|---|---|
| 1 | Permissible use | Partial |
| 2 | Informed intent | Not testable |
| 3 | Accountability/RACI | Partial |
| 4 | System boundary | Partial |
| 5 | Data governance and rights | Not testable |
| 6 | Model performance and fairness | Not testable |
| 7 | Security and misuse resistance | Not testable |
| 8 | Human oversight and stakeholder protections | Partial |
| 9 | Monitoring and lifecycle management | Not testable |
| 10 | Evidence and decision authorization | Not testable |

## Item Detail

### 1. Permissible use: Partial

**Rationale:** Route suggestion is a permissible business purpose, and the prohibited-use screen is not triggered. It stays Partial for two reasons:
- The purpose of the acceptance-rate feature is undefined.
- The employment context needs counsel review before the use can be confirmed as permissible in this configuration.

**Evidence:**
- Approved use-case statement (purpose, in-scope and out-of-scope uses, including acceptance-rate use): Requested
- Counsel memo on employment-context classification and member-state obligations: Requested

### 2. Informed intent: Not testable

**Rationale:** Authorization: **Unknown: insufficient data.** No authorization instrument was supplied, so none of the four elements can be tested:
- **Purpose:** RouteMate suggests routes. Whether it also serves as a performance signal is unstated.
- **Authority:** not stated.
- **Boundaries:** not stated. Examples: no automated route assignment; acceptance rate not used for discipline.
- **Exit:** not stated. Examples: kill switch, fallback to manual routing, decommission criteria.

The five authorizer conditions (Knowledge, Evidence, Authority, Time, Permission) also cannot be tested without a named authorizer and record.

The acceptance-rate feature is a classic site for **Inferred Intent**: a performance-management purpose nobody authorized, supplied later by the dashboard. The instrument must state its purpose explicitly.

**Evidence:**
- Signed authorization instrument (purpose, authority, boundaries, exit): Requested
- Authorizer record (delegation of authority, evidence pack reviewed, dissent and alternatives considered, review time): Requested

### 3. Accountability/RACI: Partial

**Rationale:** The Head of Operations is named as business owner. No other roles are stated (see RACI below).

**Evidence:**
- RACI matrix with named individuals: Requested

### 4. System boundary: Partial

**Rationale:**
- **Stated:** the inputs (order data, addresses, traffic feeds, driver shift times), the output (suggested routes and stop orders), the users (300 drivers, dispatch supervisors), and the supply chain (Fenwick → Corvane → third-party LLM provider).
- **Unknown: insufficient data:**
  - processing locations,
  - the identity of the LLM provider,
  - cross-border transfers and subprocessors,
  - retention,
  - access paths,
  - integrations (TMS, driver app, traffic API),
  - logging points,
  - whether free-text delivery notes are sent to the model.

**Evidence:**
- Architecture diagram: Requested
- Data-flow diagram, including transfers and subprocessors: Requested

### 5. Data governance and rights: Not testable

**Rationale:** Three categories of personal data are involved:
- recipients' names and addresses (customers),
- driver shift times (staff),
- acceptance rates (staff performance data).

The following are all **Unknown: insufficient data**: lawful basis, minimization, retention, whether Corvane or the LLM provider may use the data for training, and staff notice.

**Evidence:**
- Records of processing / data inventory: Requested
- Privacy review or DPIA screening: Requested
- Data processing agreement with Corvane, with subprocessor list: Requested
- Retention and deletion schedule: Requested

### 6. Model performance and fairness: Not testable

**Rationale:** No test results were supplied. Under risk-averse strictness, two concerns need answers.

**Fitness for purpose.** An LLM is not a route optimizer. The design must show whether the LLM wraps a deterministic solver or generates routes itself. If it generates them, the following failure modes need grounding and validation:
- non-existent or mis-geocoded stops,
- ignored time windows or vehicle limits,
- infeasible sequences.

**Fairness.** Route difficulty may be distributed unevenly across drivers, for example by part-time status, depot, or tenure. Some groups, such as drivers with disabilities or caring duties, may override suggestions more often for legitimate reasons. The acceptance-rate metric would then penalize them.

**Evidence:**
- Performance test report against baseline routing (feasibility, on-time rate, distance, shift-limit compliance): Requested
- Hallucination/grounding test report: Requested
- Route-allocation and acceptance-rate disparity analysis: Requested

### 7. Security and misuse resistance: Not testable

**Rationale:** The main threats to test are:
- **Prompt injection:** customer-controlled fields such as delivery notes or address lines could carry instructions into the model.
- **Data exfiltration:** order and address data could leak through the vendor chain.
- **Logging integrity:** acceptance-rate records are used about people, so they must be tamper-resistant.

No tool access is stated.

**Evidence:**
- Threat model and prompt-injection test results: Requested
- Vendor security assessment (Corvane and LLM provider): Requested
- Agentic controls: No evidence item: not applicable (suggestion only; no tool access stated)

### 8. Human oversight and stakeholder protections: Partial

**Rationale:**
- **Strength:** drivers can accept or change routes, so the system is suggestion-only.
- **Weakness 1:** showing supervisors each driver's acceptance rate creates pressure to accept. This can hollow out the override and turn suggestions into de facto instructions, which is automation bias by design.
- **Weakness 2:** no driver notice, explanation, or channel to contest acceptance-rate use is stated.
- **Weakness 3:** drivers may follow suggestions under time pressure, so safety and driving-time limits must be built in rather than left to review.

**Evidence:**
- Driver notice and explanation materials: Requested
- Policy restricting acceptance-rate use, with a driver contest/appeal procedure: Requested
- Worker representative consultation record (if applicable per counsel): Requested

### 9. Monitoring and lifecycle management: Not testable

**Rationale:** Nothing has been supplied on:
- SLIs/SLOs,
- drift monitoring (traffic patterns, seasonal volume),
- incident process,
- change control for vendor model updates,
- fallback to manual routing,
- review cadence,
- decommissioning.

**Evidence:**
- Monitoring plan with thresholds: Requested
- Rollback/kill-switch test record: Requested
- Vendor change-notice terms: Requested

### 10. Evidence and decision authorization: Not testable

**Rationale:** No evidence pack, deployment approver, or risk-acceptance record was supplied. Their existence is **Unknown: insufficient data**.

**Evidence:**
- Risk acceptance record: Requested
- Deployment approval sign-off: Requested

## RACI

| Role | Assignee |
|---|---|
| Business owner | Head of Operations (stated) |
| System owner | Unassigned: decision blocker |
| Model owner (incl. vendor management for Corvane) | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner (dispatch) | Unassigned: decision blocker |
| Incident/on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

## Assumptions

These are assumptions, not facts:
- **A1.** RouteMate is suggestion-only, with no tool or dispatch-system write access. This is based on "suggests" and "accept or change."
- **A2.** Rollout covers all 300 drivers, not a pilot. The rollout plan is unknown.
- **A3.** Corvane sends order and address data to the third-party LLM provider. Hosting location is unknown.
- **A4.** The acceptance rate may inform supervision of drivers. Its actual use is unknown.

**Indicative signal (not a threshold gate):** On A2 and A4, a Preliminary Intake would likely rate at least these domains Medium:
- rights impacts,
- privacy,
- safety-critical context,
- scale.

Under A2, scale could reach High. A Full Assessment would then be required.

## Confidence

- **Process conclusions (ratings and gaps):** Medium. The mock facts are clear but sparse.
- **Any system-level conclusion:** Low. There is no evidence.

**What would change the result:**
- an authorization instrument,
- a vendor data-use contract,
- a signed policy limiting acceptance-rate use,
- feasibility and fairness test reports.

## Consolidated Questions (10)

1. Which member state is it, and does Fenwick have a works council or other worker representation?
2. What exactly may supervisors do with acceptance rates? Is it used for evaluation, discipline, or pay?
3. Is RouteMate a pilot or a full rollout, and over what timeline?
4. Does the LLM generate routes directly, or wrap a routing solver?
5. Who is the LLM provider, where is data processed, and which subprocessors are involved?
6. May Corvane or the LLM provider retain or train on Fenwick data?
7. Are free-text customer fields (delivery notes) sent to the model?
8. Is driver GPS or telematics data collected or planned?
9. Are shift limits, breaks, and vehicle constraints hard-coded as constraints, or only prompted?
10. Who holds kill-switch authority, and what is the fallback routing method?

## Conclusion

**Process test completed; no system acceptance decision is possible.**

The checklist ran end to end. Four items were rated Partial and six Not testable. The decisive gaps are:
- unknown authorization (Item 2),
- unassigned roles (Item 3),
- an undefined acceptance-rate purpose that creates an employment-context risk (Items 1 and 8).

## Self-Check

- Mode stated correctly.
- Prohibited-use screen ran first.
- Assumptions are labeled and kept separate from facts.
- No inherent or residual scoring was claimed. The indicative signal is labeled as such.
- No evidence is overstated: all items are Requested.
- RACI is included.
- Legal triggers are referred to counsel.
- The conclusion matches the evidence.

---

**Status:** [↻ v1]

**Open items:**
- Authorization: Unknown: insufficient data.
- 11 RACI roles Unassigned.
- Acceptance-rate purpose undefined.
- Vendor data-use and cross-border terms unknown.
- LLM routing fitness, fairness, and security untested.
- Counsel review of employment-context obligations pending.

**Next step:** The Head of Operations should define in writing the permitted and forbidden uses of the acceptance-rate metric and name the deployment approver. This is the first input to the authorization instrument.

**Final Liability rests with the Human.**

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
