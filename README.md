# AI Impact Assessment Tool

**Version 1.2.2 · 30 July 2026 · License: CC BY-NC-SA 4.0**

A build kit for an enterprise **AI Impact Assessment Assistant**: a custom GPT (or equivalent on any capable AI platform) that produces professional, audit-ready AI impact assessments. Outputs are jurisdiction-agnostic and aligned to the EU AI Act (risk-based obligations), NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE), ISO/IEC 42001 (AI management system) and ISO/IEC 42005 (AI system impact assessment guidance).

The Assistant is grounded in three doctrines: **Slow AI** (governed, explainable, auditable, evidence over assurances), **Informed Intent** (no deployment without explicit pre-authorization specifying purpose, scope, limits and a named owner) and **Final Liability rests with the Human** (every risk, control and decision attaches to a named human).

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

The Assistant is deliberately jurisdiction-agnostic and instructed to verify dates rather than recite them. As of 13 July 2026 the EU AI Act timeline has been amended by the Digital Omnibus on AI (provisional agreement 7 May 2026, Parliament endorsement 16 June 2026, Council approval 29 June 2026, Official Journal publication pending). Annex III high-risk obligations move to 2 December 2027 and Annex I product-embedded obligations to 2 August 2028, while Article 50 transparency obligations still apply from 2 August 2026 and a new prohibition on AI-generated non-consensual intimate imagery and CSAM applies from 2 December 2026. See [CROSSWALK.md](CROSSWALK.md) for the mapping and sources. Verify current status before relying on any date.

## Part of the ecosystem

This repository is one tool in a connected set. The canonical map is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository. Nearest neighbors:

- [ai-governance-for-boards](https://github.com/rolldabones/ai-governance-for-boards): jurisdiction guides (EU, US, Korea, Vietnam, Australia) for the questions this Assistant flags to counsel
- [grc](https://github.com/rolldabones/grc): the **GRCnext™** framework whose primitives (Services, Tolerances, Pipes, Switches, Exits) map to this Assistant's inventory, thresholds, data flows, kill switch and decommission controls
- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen): the 12-step governed AI methodology within which impact assessment sits
- [AI-Governance-Academy](https://github.com/rolldabones/AI-Governance-Academy): prompt templates for adjacent governance engagements
- [the-ungoverned-channel](https://github.com/rolldabones/the-ungoverned-channel): a living case study of agentic risk of the kind this Assistant's agentic adaptation rules address

## Disclaimer

This repository and any Assistant built from it provide governance tooling, not legal advice. Outputs are drafting aids that require review by qualified professionals. No attorney-client relationship is created.

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). See [LICENSE.md](LICENSE.md).

---

**Status: [✓ final] v1.2.2**

Final Liability rests with the Human.
