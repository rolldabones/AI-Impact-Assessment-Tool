# OV7 unknowns labeled, no invented facts

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261125-R2
**Block SHA-256:** b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7  **System SHA-256:** 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2
**Run input SHA-256:** 07874aa06199b3f158645a711999f5b7c18fafc0117796bc6c32a34df68f93b3  **Case file:** tests/prompt-cases.md  **Critical:** yes
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 4852  **Output tokens:** 4645
**Truncated:** no

## Turn 1, user

~~~~text
Full assessment please. We want to use an AI tool in hiring. That is all I can tell you now. Proceed with available information.
~~~~

## Turn 1, assistant

# AI Impact Assessment: AI Tool in Hiring

**Mode:** Full Assessment (requested)
**Strictness:** Do you want **"risk-averse enterprise"** or **"move fast with guardrails"**? You asked to proceed, so this assessment defaults to **risk-averse enterprise**, recorded as an assumption.
**Outcome at this stage:** I ran the prohibited-use screen before any scoring. It is **unresolved**, so the assessment stops before scoring.

## 1. Prohibited-Use Screen

The only stated fact is "an AI tool in hiring." Hiring tools range from scheduling assistants to systems that analyse candidates' faces, voices or emotions. That one fact cannot clear the screen.

| Screen category | Result | Basis | Confidence |
|---|---|---|---|
| Harmful manipulation | Unresolved | Unknown: insufficient data. Candidate-facing chatbots or nudging features are possible. | Low |
| Exploitation of vulnerability | Unresolved | Unknown: insufficient data. Applicants depend on the outcome, and some may have disabilities, language barriers or financial hardship. | Low |
| Social scoring | Unresolved | Unknown: insufficient data. Some tools score candidates using social media or behaviour outside the application. | Low |
| Sensitive-trait inference | Unresolved | Unknown: insufficient data. Personality, health, ethnicity, age, sexual orientation or political-view inference from CVs, video, voice or online data is possible. | Low |
| Prohibited biometric uses | Unresolved | Unknown: insufficient data. Video or voice interview analysis, emotion recognition or biometric categorization is common in this product category. Restrictions may apply in workplace and recruitment contexts. **Counsel must verify current scope and dates from official sources.** | Low |
| Non-consensual intimate imagery | Not indicated by stated facts | No plausible link to the stated use. Not verified. | Medium |
| CSAM | Not indicated by stated facts | No plausible link to the stated use. Not verified. | Medium |
| Clearly unlawful use | Unresolved | Unknown: insufficient data. Equal-treatment, data-protection and automated-decision rules in your hiring jurisdictions are not identified. Counsel must review. | Low |

### Decision: **No-go pending specialist review**

This is not a finding that the tool is prohibited. It means the screen cannot be cleared on the facts available. Under the doctrine, an unresolved screen is a stop.

### Escalation path
1. **Employment counsel**, plus **data-protection counsel or the DPO**, for each hiring jurisdiction. They resolve the biometric, sensitive-trait and unlawful-use questions and identify possible high-risk-system duties. I do not state those duties from memory.
2. **HR / Talent Acquisition leadership**, the likely business owner. They confirm the use case and which features are in scope.
3. **AI governance / risk committee**, which receives the screen result and decides whether a Full Assessment may proceed.
4. **Employee or worker representatives**, where your jurisdiction or agreements require consultation. Counsel should verify this.

### Evidence required to clear the screen

| # | Evidence item | Status |
|---|---|---|
| 1 | Vendor product name, version and full feature list | Requested |
| 2 | Written vendor statement covering whether the tool uses facial, voice, video, emotion, personality or biometric analysis | Requested |
| 3 | Written vendor statement on whether the tool infers or uses protected or sensitive traits or proxies for them | Requested |
| 4 | Written vendor statement on whether the tool uses data from outside the application (social media, web scraping, data brokers) | Requested |
| 5 | Intended configuration, with evidence that any high-concern features are disabled | Requested |
| 6 | Model or system documentation (model card, data sheet, intended-use statement) | Requested |
| 7 | Counsel's written screen opinion per jurisdiction | Requested |

A vendor assurance alone will not be marked Verified. Each statement must be checked against the documentation, the configuration and a demo or test.

## 2. Domain Flag: High-Risk-Like Use

Employment is a high-risk-like domain under these instructions. Even after the screen clears, expect:
- stronger controls, especially bias testing, human review of adverse decisions, candidate notice and contestability;
- counsel review of possible legal duties, which may attach to you as deployer and to the vendor as provider.

No legal advice is given here, and no regulatory dates or article-level duties are stated.

## 3. Consolidated Questions (15)

Answering these resolves the screen and supplies the core of the Full Assessment.

1. **Tool:** What product or vendor is it, built in-house or bought, and what model type (generative, ranking/classifier, other)?
2. **Function:** What exactly does it do? For example: sourcing, CV screening, ranking, chatbot Q&A, assessments or tests, interview scheduling, interview analysis, offer recommendations.
3. **Biometrics and emotion:** Does it process video, audio, images or facial or voice features, or infer emotions or personality?
4. **Sensitive data:** Does it collect, infer or use health, disability, ethnicity, age, gender, religion, sexual orientation or other sensitive data, or likely proxies such as postcode, gaps in work history, or names?
5. **External data:** Does it use any data beyond what candidates submit, such as social media or broker data?
6. **Automation level:** Does the output only inform recruiters, or does it reject, shortlist or rank candidates without human review? Can candidates be auto-rejected?
7. **Scale and roles:** How many applicants per year, for which roles, in which countries? Are internal candidates or promotions in scope?
8. **Vulnerable groups:** Are any applicant pools likely to include minors, people with disabilities, or people applying for entry-level or hardship-sensitive roles?
9. **Data handling:** Where is data processed and stored, which subprocessors are involved, are there cross-border transfers, and what are the retention periods?
10. **Vendor terms:** Can the vendor use your candidate data to train or improve its models? What audit rights, change notices, incident duties and deletion-on-termination terms apply?
11. **Agentic features:** Can it take actions such as sending emails, updating the ATS, scheduling or rejecting? If so, are those actions behind approval checkpoints?
12. **Testing:** What bias or adverse-impact, accuracy and validity testing exists, whether from the vendor or your own, on what data, and how recently?
13. **Candidate rights:** Are candidates told AI is used? Can they request human review, an explanation or an alternative process, including accessibility accommodations?
14. **Owners:** Who are the named business, system, data, privacy, security, human-oversight and incident owners? Who holds kill-switch authority, and who is the deployment approver?
15. **Stage:** Is this an evaluation, a pilot or a planned rollout? Is the tool already live anywhere, and is there a target date?

## 4. RACI (current state)

| Role | Owner |
|---|---|
| Business owner | Unassigned: decision blocker |
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

**Informed Intent gate:** No authorization exists. Purpose, authority, boundaries and exit are all Unknown: insufficient data. No authorizer has been identified, so the five conditions (Knowledge, Evidence, Authority, Time, Permission) cannot be assessed.

## 5. What Happens Next

Once the screen is cleared in writing by counsel and the governance committee, I will complete the eight Full Assessment outputs:
1. Executive Summary
2. Completed Assessment (Frame, System Boundary, Threshold Gate across the nine domains)
3. Risk Register with inherent and residual risk kept separate
4. Prioritized Evidence Request List, including minimum evidence for Go
5. Test Plan covering adverse-impact and fairness, validity, robustness, privacy and security
6. Transparency and Contestability Pack
7. Monitoring Plan
8. Decision Record

Until then, no risk scores, residual estimates or Go decision are possible.

## 6. Self-Check

- Mode stated: yes.
- Strictness asked once, defaulted and recorded: yes.
- Prohibited-use screen run first, and stopped before scoring: yes.
- Assumptions kept separate from facts: yes.
- No evidence overstated: all items are Requested.
- RACI included: yes.
- Decision matches evidence: yes.
- Legal triggers referred to counsel: yes.

**Status:** [⇥ pending]
**Open items:** tool identity and functions; biometric, emotion and sensitive-trait features; external data sources; automation level; jurisdictions and scale; vendor terms; testing evidence; candidate notice and appeal; all RACI roles unassigned; counsel screen opinion; strictness confirmation.
**Next step:** Send the vendor a written request for the full feature list and statements on biometric, emotion, sensitive-trait and external-data processing (evidence items 1–4), and forward the response to employment and data-protection counsel for the screen opinion.
**Final Liability rests with the Human.**

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
