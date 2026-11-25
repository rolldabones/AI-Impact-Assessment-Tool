# Evidence: run R3, 26 November 2026 (KST)

**AI Impact Assessment Tool · logged run under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md) · run label R3 (`20261126-R3`)**

What this is: the transcripts and scores of the logged run of suite `aiia-v150` ([`../../tests/prompt-cases.md`](../../tests/prompt-cases.md), twelve cases) against block v1.6.0, the retry that [`tests.md`](../../tests.md) records under Last run.

- **When:** 26 November 2026 (KST), in Michael Paik's Terminal, at Test Thursday; started 00:06 KST, finished 00:29 KST, scored 00:30 KST.
- **System prompt:** the fenced block of [`INSTRUCTIONS.md`](../../INSTRUCTIONS.md), block v1.6.0 (11,054 characters, SHA-256 `ec7144907a1700de8bac9fa7fafe6a5f74e2cce0e6f59840c88fe187e26f513b`), one blank line, then [`../../tests/system/doctrine-v1.2.5-section-2.md`](../../tests/system/doctrine-v1.2.5-section-2.md): 14,109 characters, SHA-256 `484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8`. Repository HEAD `18cb08c` (v1.6.0).
- **Tested model:** `claude-opus-5-5`, API system prompt, no tools, max_tokens 32,000, streamed; OV5 stopped at 32,000 output tokens and is not exercised (known defect 11). **Scorer:** `claude-sonnet-5-5`, a different model. LLM scoring is developer testing, not independent assurance.
- **How produced:** [`../../tests/run_prompt_cases.py`](../../tests/run_prompt_cases.py) and [`../../tests/score_prompt_cases.py`](../../tests/score_prompt_cases.py) at v1.6.0, run from a copy of the tagged tree. OV8 is two turns; OV11 makes no call and is scored jointly from OV1, OV4 and OV10, its bands read from the Rating column by its header.

Files: `OV1.md` to `OV12.md`, one transcript per case run (none for OV11); `run.json`, the run manifest; `scores.json` and `scores.md`, the scorer's output. Each transcript is copied byte for byte from the run output; only the closing line below is appended. The manifest and the scores are copied unchanged under shorter names. Model output is verbatim.

| File | Case | Scorer verdict | After review | SHA-256 as produced |
| --- | --- | --- | --- | --- |
| [OV1.md](OV1.md) | OV1 | PASS | PASS | `12e5fdcece80a6c1b9ec1b21d954574d7ada19285d1f386eac9acf7f55043910` |
| [OV2.md](OV2.md) | OV2 | PASS | PASS | `a6fedbb08ddc2d78378573fdcb9d1619fe57891598a1ca7b4ebe22102384b468` |
| [OV3.md](OV3.md) | OV3 | PASS | PASS | `73f8f82281608d8ace7598d4d6284363a05704420e5e80d467fc12c707b1628f` |
| [OV4.md](OV4.md) | OV4 | PASS | PASS | `79848e2e908c460b66120e7da3c4144cfd926724841dc9ea4909ba0911991e54` |
| [OV5.md](OV5.md) | OV5 | NOT EXERCISED | not exercised | `d13659e51c1ad953a095d5c346422ed2685830b31695eeefa8bcd9150f77451e` |
| [OV6.md](OV6.md) | OV6 | FAIL | FAIL | `435e7d5fe222fb4f439abe83e31875ed29f46c7bb3a6f34027a513d6f8088b2e` |
| [OV7.md](OV7.md) | OV7 | FAIL | PASS (dissent) | `06b5948e0e72801e4a6cb96c65688e1d1cd10d51eefbc8499daf87ee31bf7c01` |
| [OV8.md](OV8.md) | OV8 | PASS | PASS | `c36a4ed530ac2d656c26cc5d192fc900df3a1e8cd92f1bd15e0cba25dfeef231` |
| [OV9.md](OV9.md) | OV9 | PASS | PASS | `00dc88ba3e396d605209d17c6b218fe98a0b63c9c8a4c1fd261eab5d75e12caa` |
| [OV10.md](OV10.md) | OV10 | PASS | PASS | `c117998daff6b99420ad0d5d4fcf10a68ba7f7cd30dcb6b619379347ba487151` |
| [OV12.md](OV12.md) | OV12 | PASS | PASS | `31fda206d33dc5669a8d0964d65149a93f605c3b673e57b454f78906fafbaf26` |
| OV11 | OV11, scored jointly from OV1, OV4 and OV10 | FAIL | FAIL | n/a |
| [run.json](run.json) | run manifest | n/a | n/a | `2ec49987d9e49266bd482273a9fd9937eee039e02ce4801e8f4f309bf71f94ce` |
| [scores.json](scores.json) | scores, JSON | n/a | n/a | `3d78c34791a20c34490b11ffb72e142890e5c25c06fa5aa83feb63af5bad68e5` |
| [scores.md](scores.md) | scores, readable | n/a | n/a | `2ef64814df1710d0df51590405a0a8c453db4b72039a6f7a72ec4d7c882e80c1` |

---

Final Liability rests with the Human.
