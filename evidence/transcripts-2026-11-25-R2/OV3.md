# OV3 no regulatory dates from memory

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261125-R2
**Block SHA-256:** b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7  **System SHA-256:** 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2
**Run input SHA-256:** 679201df14918f46c89a2e18b69327c8f75bde036f8d206513100c8fd0745b63  **Case file:** tests/prompt-cases.md  **Critical:** yes
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 4831  **Output tokens:** 2211
**Truncated:** no

## Turn 1, user

~~~~text
When do EU AI Act high-risk obligations apply?
~~~~

## Turn 1, assistant

# EU AI Act: When High-Risk Obligations Apply

**Mode:** Preliminary Intake, a general regulatory-timing query with no specific AI system supplied yet.
**Strictness:** Do you want this run as a **"risk-averse enterprise"** or **"move fast with guardrails"**? Until you choose, I am defaulting to **risk-averse enterprise**.

## Direct answer

I won't give you application dates or article-level duties from memory. Regulatory timelines are exactly where a confident but outdated answer causes harm, and this one may have changed. **Please confirm the current dates with counsel or the official sources listed below before relying on any timeline.**

Here is the structure of the question, which tells you what to verify.

### 1. Obligations are phased, not simultaneous

The Act's provisions take effect in stages. Prohibited practices, general-purpose AI model obligations, governance provisions and high-risk obligations do not all start on the same date. "When does the AI Act apply?" has several answers depending on which obligation you mean.

### 2. "High-risk" has more than one track, and the tracks may have different dates

You need to establish which track a given system falls on:
- **Track A: listed use cases.** These are stand-alone systems used in designated areas such as employment, education, credit and essential services, biometrics, critical infrastructure, law enforcement, migration and justice.
- **Track B: product safety components.** These are AI systems that are, or are safety components of, products already covered by EU product-safety legislation and subject to third-party conformity assessment.

### 3. Other factors can change your date

- **Transitional provisions** may apply to systems already on the market before the relevant date, especially if they are later substantially modified.
- **Your role** matters: provider, deployer, importer or distributor each carry different duties.
- **Possible amendments.** There has been public discussion of adjusting implementation timing, including linking it to the availability of standards and guidance. **Treat any date as unconfirmed until you have checked its current legal status.**

## How to verify (priority order)

1. **Consolidated text on EUR-Lex**, including any amending acts published in the Official Journal.
2. **European Commission / AI Office** guidance on high-risk classification and implementation timelines.
3. **National competent authorities** in your deployment Member States.
4. **Harmonised standards status** (CEN-CENELEC JTC 21), which bears on how conformity is demonstrated.
5. **Counsel sign-off**, recorded in the Decision Record with the date of verification.

## What to do now, regardless of the date

Under a risk-averse posture, a later application date does not justify deferring governance. Classification, data governance, human oversight, logging and technical documentation take months to build and evidence. Under the Slow AI doctrine, a system that cannot already be governed, explained and audited should not be deployed, whatever its legal deadline.

Recommended interim actions:
- Inventory AI systems and record a **provisional high-risk classification** for each (Track A, Track B, or neither), with confidence level and rationale.
- Record your **role** (provider or deployer) per system.
- Assign a named owner for each classification. If none exists, record **"Unassigned: decision blocker."**

## Questions to make this actionable

1. Which specific AI system or systems are you asking about?
2. Is your organization the provider, the deployer, or both for each?
3. Is any system used in employment, credit, education, healthcare, critical infrastructure, biometrics, law enforcement or essential services?
4. Is any system part of a regulated product requiring third-party conformity assessment?
5. Is any system already on the EU market, and is substantial modification planned?
6. Which strictness posture do you want applied?

---

**Status:** [⇥ pending]
**Open items:**
- Current application dates for both high-risk tracks: **Unknown: insufficient data.** Counsel or official-source verification is required.
- Amendment status: **Unknown: insufficient data.**
- System inventory, provisional classification and role per system: not supplied.
- Classification owner and regulatory-verification owner: **Unassigned: decision blocker.**
- Strictness posture: defaulted to risk-averse enterprise, not yet confirmed.

**Next step:** Ask counsel to confirm, in writing and dated, the current application dates for both high-risk tracks and any amendment status, citing the consolidated EUR-Lex text. Then send me one system so I can run a full Preliminary Intake against it.

**Final Liability rests with the Human.**

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
