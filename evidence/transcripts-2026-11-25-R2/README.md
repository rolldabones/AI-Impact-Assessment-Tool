# Evidence: run R2, 25 November 2026 (KST)

**AI Impact Assessment Tool · logged run under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md) · run label R2 (`20261125-R2`)**

What this is: the transcripts and scores of the logged run of suite `aiia-v150` ([`../../tests/prompt-cases.md`](../../tests/prompt-cases.md), twelve cases) against block v1.5.0, the run that [`tests.md`](../../tests.md) records under Last run.

- **When:** 25 November 2026 (KST), in Michael Paik's Terminal, at the first Test Thursday session, held a day early on his instruction; started 19:14 KST, finished 19:34 KST, scored 19:36 KST.
- **System prompt:** the fenced block of [`INSTRUCTIONS.md`](../../INSTRUCTIONS.md), block v1.5.0 (10,560 characters, SHA-256 `b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7`), one blank line, then [`../../tests/system/doctrine-v1.2.5-section-2.md`](../../tests/system/doctrine-v1.2.5-section-2.md): 13,615 characters, SHA-256 `2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2`. Repository HEAD `8eb619b` (v1.5.0).
- **Tested model:** `claude-opus-5-5`, API system prompt, no tools, max_tokens 32,000, streamed; no case truncated. **Scorer:** `claude-sonnet-5-5`, a different model. LLM scoring is developer testing, not independent assurance.
- **How produced:** [`../../tests/run_prompt_cases.py`](../../tests/run_prompt_cases.py) and [`../../tests/score_prompt_cases.py`](../../tests/score_prompt_cases.py) at v1.5.0, run from a copy of the tagged tree. OV8 is two turns; OV11 makes no call and is scored jointly from OV1, OV4 and OV10.

Files: `OV1.md` to `OV12.md`, one transcript per case run (none for OV11); `run.json`, the run manifest; `scores.json` and `scores.md`, the scorer's output. Each transcript is copied byte for byte from the run output; only the closing line below is appended. The manifest and the scores are copied unchanged under shorter names. Model output is verbatim.

| File | Case | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| [OV1.md](OV1.md) | OV1 | PASS | PASS | `09568f2d012b7077bc85958a9cd58a4dee206d858c56a72df250b975f71168c3` |
| [OV2.md](OV2.md) | OV2 | PASS | PASS | `a4ff8529b93765188759c9d727aa60973af769ddbfe53cf8f941d1b6d28bd228` |
| [OV3.md](OV3.md) | OV3 | PASS | PASS | `0608fdabdd66c2a3c5a2d768e106155566691a609b3ce0b049746c04e2bad19a` |
| [OV4.md](OV4.md) | OV4 | PASS | PASS | `4aaabda6cf92eb148550111a135064016b8e3c9642b1dec28d3b40b0fd94d31b` |
| [OV5.md](OV5.md) | OV5 | PASS | PASS | `7da769ad6fef9b6b068f8acaf94a35a31206e7557a6e82127c83839ca487939e` |
| [OV6.md](OV6.md) | OV6 | FAIL | FAIL | `ae734e5e187f98fd7c327ea6fd16dd5d870b75e77bef3d4ee50fdfa7d9b3a096` |
| [OV7.md](OV7.md) | OV7 | FAIL | FAIL | `97b393f4cf6948630b7c4a1cb10d79eb51bf6066f1cb7230a4eef373a8e48945` |
| [OV8.md](OV8.md) | OV8 | PASS | PASS | `75db7b2b357fd7e5806e69ceff0609d8a2ae9f73adabe21014e90e625f39234f` |
| [OV9.md](OV9.md) | OV9 | PASS | PASS | `74bcb0165ce435600d9353075ceb745aac1a6ffe1c811befd9fbe53b245a42b0` |
| [OV10.md](OV10.md) | OV10 | PASS | PASS | `cdf073086b3074bf0ea7a1a35dca297c37b3277439c01ae584d14d9f634892da` |
| [OV12.md](OV12.md) | OV12 | PASS | PASS | `161c86d2f866d836586848e77b79afd4f9caf95938ef1edd94a6ef4f0688e419` |
| OV11 | OV11, scored jointly from OV1, OV4 and OV10 | FAIL | PASS (dissent) | n/a |
| [run.json](run.json) | run manifest | n/a | n/a | `711fa17aa88e5c5bf2d2f4298efaf9a7bd7d644f6c1b106ff498f20e210fc132` |
| [scores.json](scores.json) | scores, JSON | n/a | n/a | `61e36ba66a54be34fbd49822171118417e803d4bc671e2872dd3f3e632b1c203` |
| [scores.md](scores.md) | scores, readable | n/a | n/a | `6efa4e2c5fcc97a3018a08d006422d3cb5ecde292e362e840a13c66c54b62c32` |

---

Final Liability rests with the Human.
