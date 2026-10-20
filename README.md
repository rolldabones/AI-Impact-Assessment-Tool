# AI Impact Assessment Tool

**Version 1.4.2 · 20 October 2026 · Instrument, formerly the AI Impact Assessment Assistant custom GPT (retired 1 October 2026) · Instructions last verified against the GPT on 13 July 2026, before the conversion · License: [CC BY-NC-SA 4.0](LICENSE.md)**

> **Retired 1 October 2026 (Korea Standard Time, KST).** The AI Impact Assessment Assistant custom GPT was retired on 1 October 2026 and converted to a private plug-in on the OpenAI platform. The instructions published in this repository are the text of record and suffice for anyone who wants to build their own. History and sources: [RETIREMENT.md](https://github.com/rolldabones/rolldabones/blob/main/RETIREMENT.md).

## What it does

An instruction block that turns any current assistant into an enterprise **AI Impact Assessment Assistant**, producing professional, audit-ready AI impact assessments. Outputs are jurisdiction-agnostic and aligned to the EU AI Act (risk-based obligations), NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE), ISO/IEC 42001 (AI management system) and ISO/IEC 42005 (AI system impact assessment guidance).

The Assistant is grounded in three doctrines: **Slow AI** (governed, explainable, auditable, evidence over assurances), **Informed Intent** (prior authorization with the elements and conditions stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md)) and **Final Liability rests with the Human** (every risk, control and decision attaches to a named human).

## Who this is for

Enterprise governance, risk management and compliance teams, in-house counsel, AI product owners and internal auditors who need repeatable, evidence-led impact assessments, whether or not the operator has been trained in AI impact assessment. The Assistant is not a lawyer and not the final approver. It labels missing facts Unknown/Insufficient data and it never states regulatory application dates from memory.

## What the Assistant produces

1. Executive Summary with risk classification and key conditions
2. Completed Assessment (System, Data, Model, Workflow, Stakeholders, Risks and Controls)
3. Risk Register (Risk | Inherent | Controls | Evidence | Residual | Owner | Status)
4. Prioritized Evidence Request list with a minimum-evidence-for-Go checklist
5. Test Plan (fairness, performance, robustness, privacy and security, monitoring thresholds)
6. Transparency and Contestability pack (notices, explanation template, appeal steps)
7. Monitoring and Continuous Improvement plan (service level indicators and objectives, SLIs/SLOs; drift, incidents, change control, decommission)
8. Decision Record (Go; Go with conditions; No-go; No-go pending specialist review; No decision possible: insufficient evidence; with assumptions, confidence, sign-offs and revalidation triggers)

A prohibited-use screen runs before any scoring. Every evidence item is tagged Requested / Provided / Verified / Not verified. Inherent and residual risk are always separated.

## Run it in three steps

1. Paste the fenced block in [INSTRUCTIONS.md](INSTRUCTIONS.md) (7,657 characters) into the system prompt, custom instructions or project instructions of any current assistant. [CROSSWALK.md](CROSSWALK.md) may be attached as a reference file if wanted; the block does not require it.
2. Give it the inputs it asks for (at most 15 consolidated questions and your strictness preference), or start from [example.md](example.md).
3. Review the output yourself and check it against the [Operator verification checklist](INSTRUCTIONS.md#operator-verification-checklist). Keep your own run log: [tests.md](tests.md) is this repository's record of its runs and shows the format. You own sign-off.

To reproduce or adapt the build process itself, read [BUILD-GUIDE.md](BUILD-GUIDE.md).

## Files

| File | Purpose |
|---|---|
| [README.md](README.md) | This overview |
| [INSTRUCTIONS.md](INSTRUCTIONS.md) | The instruction block (the instrument) plus the operator verification checklist |
| [tests.md](tests.md) | The test cases, known defects and the record of logged runs |
| [example.md](example.md) | One illustrative run on fictional inputs |
| [BUILD-GUIDE.md](BUILD-GUIDE.md) | Step-by-step account of how the Assistant was built and improved, and how to build it now |
| [CROSSWALK.md](CROSSWALK.md) | Mapping of Assistant outputs to EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005, with a dated regulatory-currency note |
| [CHANGELOG.md](CHANGELOG.md) | Version history, including the configuration as last deployed |
| [CITATION.cff](CITATION.cff) | Machine-readable citation |
| [LICENSE.md](LICENSE.md) | CC BY-NC-SA 4.0 notice |

## Standards and regulatory currency

The Assistant is deliberately jurisdiction-agnostic and instructed to verify dates rather than recite them.

**Amendment note, 13 August 2026 (KST).** The Digital Omnibus on AI amending Regulation (EU) 2024/1689 **entered into force on 27 July 2026**. The deferred dates below are therefore operative law, not pending changes. This paragraph previously described publication as pending. Annex III stand-alone high-risk obligations are deferred to 2 December 2027 and Annex I product-embedded obligations to 2 August 2028. Article 50 transparency obligations apply from 2 August 2026 for providers and deployers, with one carve-out: providers of generative systems placed on the market before 2 August 2026 have until 2 December 2026 to meet the Article 50(2) machine-readable marking duty (Article 111(4) of Regulation (EU) 2024/1689, inserted by Regulation (EU) 2026/1744, Article 1, point (39)(b); Recital 38 gives the context; this sentence cited Recital 38 alone until 20 October 2026 (KST)). Two new prohibitions, Article 5(1), first subparagraph, points (ba) and (bb), on AI-generated non-consensual intimate imagery and child sexual abuse material, apply from 2 December 2026 (this note read "a new prohibition" until 15 October 2026 (KST)). The canonical account-wide statement of the post-Omnibus timeline is the [EU AI Act currency note](https://github.com/rolldabones/ai-governance-for-boards/blob/main/05-jurisdictions/eu.md#eu-ai-act-currency-note) in ai-governance-for-boards, dated 15 October 2026 (KST); where this paragraph and that note differ, the note governs. Article 5 sits in Chapter II. Under **Article 113, third paragraph, point (a)**, as replaced by Regulation (EU) 2026/1744, Chapters I and II apply from **2 February 2025**, **with the exception of Article 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b), which apply from 2 December 2026**. So the general Article 5 date is 2 February 2025 and the prohibitions added by the Omnibus are deferred to 2 December 2026. Do not state the Article 5 date without that carve-out. See [CROSSWALK.md](CROSSWALK.md) for the mapping, the coverage boundary and the sources.

**Scope, informed by the crosswalk.** The crosswalk maps this Assistant's workflow onto the EU AI Act, the NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005. What the mapping does not reach is as material as what it does: the Assistant supports an impact assessment, it does not perform a conformity assessment, issue a declaration of conformity or discharge any obligation owed to a regulator. Read the crosswalk for the boundary before relying on the output as evidence.

## Change control

The custom GPT configuration is Locked as of 1 October 2026. It ran block v1.2.1, last verified on 13 July 2026, on the model recorded as GPT-5.2 Thinking; that configuration is archived in [CHANGELOG.md](CHANGELOG.md) v1.3.0. Changes are now made in [INSTRUCTIONS.md](INSTRUCTIONS.md) under this repository's release rule. A changed block is accepted only after one logged run of the published instructions as a system prompt on a current frontier model, recorded in [tests.md](tests.md). The first such run, T5 on 18 October 2026 (KST) on `claude-opus-5-5`, passed all ten cases of the operator verification checklist on block v1.4.0; Michael Paik reviewed the run on 19 October 2026 (KST) and accepted block v1.4.0, as [tests.md](tests.md) records.

## Part of the ecosystem

This repository is one tool in a connected set. The canonical map is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

The three doctrines are used in this repository as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement. Where this repository restates a doctrine, it restates it at its own altitude and adds instruments, not doctrine (ECOSYSTEM.md protocol item 6).

Nearest neighbors:

- [ai-governance-for-boards](https://github.com/rolldabones/ai-governance-for-boards): jurisdiction guides (EU, US, Korea, Vietnam, Australia) for the questions this Assistant flags to counsel
- [grc](https://github.com/rolldabones/grc): the **GRCnext™** framework whose primitives (Services, Tolerances, Pipes, Switches, Exits) map to this Assistant's inventory, thresholds, data flows, kill switch and decommission controls
- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen): the 12-step governed AI methodology within which impact assessment sits
- [AI-Governance-Academy](https://github.com/rolldabones/AI-Governance-Academy): prompt templates for adjacent governance engagements
- [the-ungoverned-channel](https://github.com/rolldabones/the-ungoverned-channel): a living case study of agentic risk of the kind this Assistant's agentic adaptation rules address

## Disclaimer

This repository and any Assistant built from it provide governance tooling, not legal advice. Outputs are drafting aids that require review by qualified professionals. No attorney-client relationship is created.

## How to Cite

> Paik, Son-U Michael. *AI Impact Assessment Tool*, v1.4.2. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Impact-Assessment-Tool

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). See [LICENSE.md](LICENSE.md).

---

**Status: [✓ final] v1.4.2**

Final Liability rests with the Human.
