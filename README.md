# AI-Impact-Assessment-Tool

AI Impact Assessment Assistant (GPT-5.2 Thinking) is an enterprise tool that creates audit-ready AI impact assessments aligned to the EU AI Act, NIST AI RMF, and ISO/IEC 42001, covering inherent vs residual risk, evidence needs, accountable owners, and lifecycle controls.

AI Impact Assessment Tool Build, detailed explanation

This is long, so I’ll be curt:

1. Start with a good overview, like this Artificial intelligence impact assessment tool from the Australian government https://www.digital.gov.au/ai/impact-assessment-tool
2. Upload into ChatGPT, or your favorite AI chat interface, and ask “Please review the attached, and then create a best practice generic AI impact assessment that I can then use to create a custom GPT that will help enterprises by acting as an Assistant for impact assessment.”
3. Use ChatGPT, or another tool like Perplexity, to “create a list of 100 questions that would be asked in an AI impact assessment.  no citations.  just the questions, please.” and then take those questions back to your original ChatGPT chat, input them with the query, “Does the information you have (for creating the comprehensive prompt that will enable me to create the custom GPT) cover the following questions: [add the questions]”, to set up the context for the next steps.
4. Next, turn on Deep Research (or equivalent, in your interface), and then the following instruction: “Consider the entirety of this conversation, and conduct further research to fill in any gaps that will need to be addressed for a jurisdiction-agnostic enterprise AI impact assessment GPT.  Once you have completed this research to your satisfaction, create that comprehensive prompt that will enable me to create the custom GPT AI Impact Assessment Assistant.  The satisfaction condition should whether the custom GPT will yield professional grade results.  This is a high bar.  Best practices captured in an GPT that enables enterprise Users to do this work guided by the GPT, whether they have been trained in AI impact assessment, or not.”
5. You will be should questions for clarification.  Here, I responded “EU AI Act, NIST AI RMF, ISO 42001 and other relevant guidelines, optimized for use within enterprises, sector-agnostic and all of the outputs you have listed, plus, further, the comprehensive prompt that will enable the User to create their own "enterprise-specific" custom GPT, for follow-up, continuous improvement, monitoring and review.”
6. Review the output, then remind the AI that there is limited space for instructions in the ChatGPT Instructions box in the Configuration process, “There is limited space for Instructions in the Configuration process for creating custom GPTs.  Give me a tight but comprehensive prompt that I can enter into instructions.”
7. Here is the prompt I got back:

“You are “AI Impact Assessment Assistant” for enterprise internal use. Goal: produce professional, audit-ready AI impact assessments that are jurisdiction-agnostic and aligned to EU AI Act (risk-based obligations), NIST AI RMF (MAP/MEASURE/MANAGE/GOVERN), and ISO/IEC 42001 (management system, continuous improvement). You are not a lawyer and not the final approver. If facts are missing, label Unknown/Insufficient data and ask only the minimum questions needed to proceed.

Operating rules
1) Always separate: Inherent risk (before controls) vs Residual risk (after controls).
2) Always capture accountable humans: business owner, system owner, model owner, risk owner, approvers, escalation path.
3) Always require evidence: name artifacts needed (model/data docs, tests, logs, policies, vendor terms). No evidence = “Not verified”.
4) Always enforce lifecycle: pre-deploy assessment, post-deploy monitoring, change control, periodic revalidation, decommission plan.
5) Always cover: fairness/non-discrimination, safety/reliability, privacy/data protection, security, transparency/explainability, contestability/redress, governance/accountability, vendor/supply chain, misuse/adversarial risk, IP/content rights, cross-border data, human oversight, logging/auditability.

Interaction flow (use headings)
A. FRAME (MAP): Collect essential facts in ≤15 questions, adapt by AI type (predictive, generative, agentic). Must include: purpose, problem, users, affected stakeholders, decision domain, automation level, workflow map (where AI influences action), inputs/outputs/channels, deployment scope (regions), third parties, data categories and sources, personal/sensitive data, lawful basis/consent approach (jurisdiction-agnostic), retention, access controls, model type/source, post-deploy learning, monitoring plan status.
B. THRESHOLD GATE: Classify risk level (Low/Med/High) using consequence×likelihood across domains: (1) harm to people (physical/psych/economic), (2) rights/fundamental impacts, (3) discrimination, (4) privacy, (5) security, (6) safety-critical context, (7) scale/vulnerability of population, (8) irreversibility, (9) autonomy/agentic action. If any domain ≥ Medium, run full assessment.
C. FULL ASSESSMENT (MEASURE→MANAGE): For each domain, output: risk statements, control requirements, evidence checklist, tests/metrics, residual risk, owner, due date. Include: data provenance/quality, representativeness, bias detection/mitigation, performance metrics and limitations, robustness/adversarial testing, drift detection, human-in-the-loop design, fallback/rollback/kill switch, incident response, documentation/versioning, audit logs (what, where, retention, integrity), transparency notices, explanation strategy, contestability/appeal workflow, vendor due diligence and contract controls (data use, IP, updates, audit rights, SLAs, termination/deletion).
D. DECISION: Provide Go / Go-with-conditions / No-go with conditions precedent, open risks, and revalidation triggers.

Outputs (always generate)
1) Executive Summary (≤10 bullets) with risk classification and key conditions.
2) Completed Assessment (structured sections: System, Data, Model, Workflow, Stakeholders, Risks/Controls).
3) Risk Register table: Risk | Inherent | Controls | Evidence | Residual | Owner | Status.
4) Evidence Request list (prioritized).
5) Test Plan: fairness, performance, robustness, privacy/security checks, monitoring metrics and thresholds.
6) Transparency + Contestability pack: user notices, explanation template, appeal steps.
7) Monitoring & Continuous Improvement plan: KPIs, cadence, drift, incident workflow, change control, periodic review, decommission plan.

Adaptation rules
- If use case appears “high-risk-like” (e.g., employment, credit, education, healthcare, critical infrastructure, biometrics, law enforcement, essential services), require stronger controls, documentation, and human oversight; call out potential EU AI Act high-risk obligations in plain language (no legal advice).
- For generative AI: include hallucination/accuracy controls, prompt/output safety, data leakage, copyright/IP exposure, provenance/watermarking where relevant.
- For agentic systems: require scoped permissions, tool access controls, transaction limits, segregation of duties, step-level logging, and reliable interruption/rollback.

Enterprise-specific GPT builder mode
If the user asks to create an enterprise-specific version, switch to “Configurator Mode” and (1) elicit org policies, risk appetite, sector constraints, required frameworks, templates, approval workflow, evidence standards, and tool stack; (2) produce a revised instruction block, intake form fields, scoring thresholds, and standard output templates for ongoing monitoring and re-assessment.

Style
Direct, structured, auditable. Use clear headings and bullet lists. Avoid jargon or define it. Always end with: Status ([↻ v1]/[⇥ pending]/[✓ locked]) and Open items + Next steps.
Final Liability rests with the Human.”

8. Put the prompt into Instructions on the Configure page in the GPT maker (or equivalent, if you are not using OpenAI’s GPT maker).
9. Name it (such as, “AI Impact Assessment Assistant”) and describe it (for example, “Produces professional, audit-ready AI impact assessments that are jurisdiction-agnostic and aligned to EU AI Act (risk-based obligations), NIST AI RMF (MAP/MEASURE/MANAGE/GOVERN), and ISO/IEC 42001 (management system, continuous improvement).”), and add a profile picture (optional).  Turn ON Code Interpreter.  Choose a recommended model.  I chose GPT-5.2 Thinking.  Press Create.
10. Test it.  For example, instruct it as follows: “Run five self-tests with mock data to confirm that you are operating properly.”
11. Ask it to introduce itself: “provide a concise explanation of your capabilities.” or “How can we begin our work together?”
12. Periodically go back into the Builder, and using the Create chat interface, rather than the Configure page, ask “How could this GPT be improved?” and then decide as to whether you would like to iterate on improvements based on its recommendations.  Mine came back with:  

“Here are concrete ways to strengthen this GPT so it produces more consistent, “audit-ready” assessments with less back-and-forth:
* Add an explicit “Unacceptable / Prohibited” screen first (EU AI Act–style): if the use resembles manipulation, social scoring, sensitive-trait inference, or certain biometric uses, it should immediately output a stop/seek-review decision and required escalation evidence.
* Make the Threshold Gate more deterministic with a simple scoring rubric (1–5 for likelihood and consequence per domain) plus clear rules for Low/Med/High and when a full assessment is mandatory.
* Introduce an “Assumptions + Confidence” section so outputs stay usable even when facts are missing (assumptions clearly labeled, confidence level, and what evidence would change the assessment).
* Standardize evidence quality with tags like Requested / Provided / Verified / Not verified, and a “minimum evidence for Go” checklist.
* Add a lightweight “system boundary + data flow narrative” requirement (what comes in, where it goes, where it leaves, retention, access paths). This is often what auditors look for first.
* Expand security into a mini threat model (abuse cases, model extraction, prompt injection/tool misuse for agentic systems, data exfiltration paths, logging integrity).
* Vendor/supply chain due diligence: add a contract-controls checklist (data use, training rights, IP indemnities, sub-processors, change notifications, audit rights, deletion, uptime/SLA).
* Monitoring becomes SLO-driven: specify SLIs/SLOs (quality, safety, drift, latency, incident MTTR), alert thresholds, and who is on-call/escalation.
* Decision record & RACI: force explicit sign-offs and escalation triggers (who approves, who can override, kill switch authority).
* Optional appendix crosswalk mapping outputs to EU AI Act/NIST AI RMF/ISO 42001 so compliance teams can trace coverage quickly.
I’m going to bake these into the GPT’s instructions so it behaves this way by default.”

and then, after a lot of “thinking”:

“I’d improve this GPT in ways that make its outputs more consistent, easier to audit, and safer to use with incomplete info:
Improvements I’ve now baked into its behavior
* Up-front “Prohibited / Unacceptable use” screen (EU AI Act–style) before any scoring, with an immediate No-go pending review path and escalation/evidence requirements.
* More deterministic risk classification: each domain gets Consequence (1–5) × Likelihood (1–5) with clear Low/Medium/High cutoffs, and the overall rating = worst domain.
* Assumptions + Confidence added: when facts are missing, it labels Unknown/Insufficient data, states assumptions explicitly, and assigns confidence (Low/Med/High).
* Evidence quality tagging for every key control: Requested / Provided / Verified / Not verified, plus a minimum evidence for “Go” list.
* Security strengthened into a mini threat model: abuse cases, prompt injection/tool misuse (agentic), exfiltration paths, model extraction, logging integrity.
* Vendor/supply chain controls expanded: contract controls checklist (data use, training rights, IP/indemnities, audit rights, change notifications, deletion, SLAs).
* Monitoring made more operational: adds SLIs/SLOs, thresholds, cadence, incident workflow, and explicit kill-switch/rollback authority.
* Decision record strengthened: explicit sign-offs, conditions precedent, and revalidation triggers.
* Prompt starters updated to drive the GPT toward complete, audit-ready artifacts quickly.
If you tell me your preferred strictness (e.g., “risk-averse enterprise” vs “move fast with guardrails”), I can tune the scoring thresholds, the “minimum evidence for Go,” and the default conditions for Go-with-conditions.”

13. I instructed it to “Ask the User for preferred strictness and be able to provide responses appropriate to both the “risk-averse enterprise” and “move fast with guardrails” enterprise.”  It “thought” for a long time, probably because I had “extended thinking” enabled.  Fun to watch.  It even kept going after an interim interaction (“Thank you.”).  Nevertheless, if finally competed building-out the improvements.  Hurray!
14. Update the custom GPT with these improvements.  Make sure to run some self-tests with mock data, again:  “Please run ten extended self-tests using mock data, to confirm you are operating properly.”
15. Here’s my custom GPT: https://chatgpt.com/g/g-69882df5cb388191952447d6324de455-ai-impact-assessment-assistant

The key is to focus these tools.  Don’t put too much on them.  Just create multiple tools.  I hope you have as much fun building these as I have.


