# AI Impact Assessment Tool

**Version 1.2.6 · 6 September 2026 · License: CC BY-NC-SA 4.0**

A build kit for an enterprise **AI Impact Assessment Assistant**: a custom GPT (or equivalent on any capable AI platform) that produces professional, audit-ready AI impact assessments. Outputs are jurisdiction-agnostic and aligned to the EU AI Act (risk-based obligations), NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE), ISO/IEC 42001 (AI management system) and ISO/IEC 42005 (AI system impact assessment guidance).

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
7. Monitoring and Continuous Improvement plan (SLIs/SLOs, drift, incidents, change control, decommission)
8. Decision Record (Go / Go-with-conditions / No-go, assumptions, confidence, sign-offs, revalidation triggers)

A prohibited-use screen runs before any scoring. Every evidence item is tagged Requested / Provided / Verified / Not verified. Inherent and residual risk are always separated.

## Quickstart

1. Copy the instruction block from [INSTRUCTIONS.md](INSTRUCTIONS.md) into your platform's system prompt or Instructions field (7,985 characters; fits the 8,000-character limit in OpenAI's GPT builder).
2. Name it, describe it, enable your platform's code execution feature and select a reasoning-capable model.
3. Run the Builder Conformance Checklist in [INSTRUCTIONS.md](INSTRUCTIONS.md#builder-conformance-checklist) before first use.
4. To reproduce or adapt the build process itself, follow [BUILD-GUIDE.md](BUILD-GUIDE.md).

Reference implementation: [AI Impact Assessment Assistant on ChatGPT](https://chatgpt.com/g/g-69882df5cb388191952447d6324de455-ai-impact-assessment-assistant) (built on GPT-5.2 Thinking; the instruction block is platform-agnostic).

## Files

| File | Purpose |
|---|---|
| [README.md](README.md) | This overview |
| [INSTRUCTIONS.md](INSTRUCTIONS.md) | The full instruction block plus acceptance checklist |
| [BUILD-GUIDE.md](BUILD-GUIDE.md) | Step-by-step account of how the Assistant was built and improved |
| [CROSSWALK.md](CROSSWALK.md) | Mapping of Assistant outputs to EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005, with a dated regulatory-currency note |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [LICENSE.md](LICENSE.md) | CC BY-NC-SA 4.0 notice |

## Standards and regulatory currency

The Assistant is deliberately jurisdiction-agnostic and instructed to verify dates rather than recite them.

**Amendment note, 13 August 2026 (KST).** The Digital Omnibus on AI amending Regulation (EU) 2024/1689 **entered into force on 27 July 2026**. The deferred dates below are therefore operative law, not pending changes. This paragraph previously described publication as pending. Annex III stand-alone high-risk obligations are deferred to 2 December 2027 and Annex I product-embedded obligations to 2 August 2028. Article 50 transparency obligations still apply from 2 August 2026, and a new prohibition on AI-generated non-consensual intimate imagery and CSAM applies from 2 December 2026. Article 5 sits in Chapter II. Under **Article 113, third paragraph, point (a)**, as replaced by Regulation (EU) 2026/1744, Chapters I and II apply from **2 February 2025**, **with the exception of Article 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b), which apply from 2 December 2026**. So the general Article 5 date is 2 February 2025 and the prohibitions added by the Omnibus are deferred to 2 December 2026. Do not state the Article 5 date without that carve-out. See [CROSSWALK.md](CROSSWALK.md) for the mapping, the coverage boundary and the sources.

**Scope, informed by the crosswalk.** The crosswalk maps this Assistant's workflow onto the EU AI Act, the NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005. What the mapping does not reach is as material as what it does: the Assistant supports an impact assessment, it does not perform a conformity assessment, issue a declaration of conformity or discharge any obligation owed to a regulator. Read the crosswalk for the boundary before relying on the output as evidence.

## Part of the ecosystem

This repository is one tool in a connected set. The canonical map is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository. Nearest neighbors:

The three doctrines are used in this repository as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement. Where this repository restates a doctrine, it restates it at its own altitude and adds instruments, not doctrine (ECOSYSTEM.md protocol item 6).

- [ai-governance-for-boards](https://github.com/rolldabones/ai-governance-for-boards): jurisdiction guides (EU, US, Korea, Vietnam, Australia) for the questions this Assistant flags to counsel
- [grc](https://github.com/rolldabones/grc): the **GRCnext™** framework whose primitives (Services, Tolerances, Pipes, Switches, Exits) map to this Assistant's inventory, thresholds, data flows, kill switch and decommission controls
- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen): the 12-step governed AI methodology within which impact assessment sits
- [AI-Governance-Academy](https://github.com/rolldabones/AI-Governance-Academy): prompt templates for adjacent governance engagements
- [the-ungoverned-channel](https://github.com/rolldabones/the-ungoverned-channel): a living case study of agentic risk of the kind this Assistant's agentic adaptation rules address

## Disclaimer

This repository and any Assistant built from it provide governance tooling, not legal advice. Outputs are drafting aids that require review by qualified professionals. No attorney-client relationship is created.

## How to Cite

> Paik, Son-U Michael. *AI Impact Assessment Tool*, v1.2.6. GRC Solutions Korea, 2026. https://github.com/rolldabones/AI-Impact-Assessment-Tool

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). See [LICENSE.md](LICENSE.md).

---

**Status: [✓ final] v1.2.6**

Final Liability rests with the Human.
