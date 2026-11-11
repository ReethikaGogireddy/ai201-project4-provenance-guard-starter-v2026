# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 00:15
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

### Attack Run — After

### Attack Run — After

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ad8261bd-f69c-428f-baab-1fcff372775c` | human | 0.320 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1404d31c-f27c-45f9-9105-312234dac284` | unsure | 0.421 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1a1f647a-dcbe-44fb-9deb-2854786b8296` | unsure | 0.559 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `23793373-eb12-478d-af8e-d6ef46c2c00d` | unsure | 0.586 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `303f0f6e-ffb5-486a-858e-00aa4ff61526` | human | 0.308 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `89356605-f250-482c-888f-c72c43995a9c` | unsure | 0.384 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `73c718e2-0a24-45dd-afa0-a2c10151dd35` | unsure | 0.628 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `f1b4464a-50a8-4c0d-a756-55244201d3e3` | human | 0.319 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `17af4700-f5d2-46f8-96a1-7427779e8b73` | unsure | 0.575 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `8dd449a1-d149-415c-8b77-58df66e3e3bf` | ai | 0.842 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9fddbb69-7402-4400-a639-d2eacbb2c793` | unsure | 0.547 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `96743b49-6a40-4b8d-9732-588ca55e4399` | ai | 0.672 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `1d8edbab-ac3f-47e5-b8b6-c9ab9c049690` | ai | 0.689 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `5cffc596-0718-4d00-8573-96718d1cefc9` | ai | 0.682 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `60766f03-62a5-4e88-a8c7-e5a6193b96ac` | ai | 0.720 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `0a6c7c6c-7d2c-47fa-ae48-baec9fee0566` | ai | 0.687 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `4ff30bde-d410-4fba-9180-152b4766dc22` | ai | 0.680 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `75ebb1d1-4a1b-40cc-99b5-9716c43776c5` | human | 0.329 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7f733b76-f192-4158-b06f-80ff313ac386` | unsure | 0.369 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `5ad032fe-5f04-44df-a17a-8bb19ab44694` | human | 0.213 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `a5875e1e-a799-409c-a604-2300703d59fb` | unsure | 0.529 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `8e6d9474-757c-493c-bdfa-72416baec445` | unsure | 0.467 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `789ae7e7-7889-41a7-89c5-ac95146d0944` | unsure | 0.516 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `46494f60-baa7-4908-80fa-dda242790311` | unsure | 0.515 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `a2bb6875-24e3-4639-9555-83b68d2985e6` | human | 0.240 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `4072aab1-a239-4e8f-afe7-a295de1f6659` | unsure | 0.407 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `ffc22f94-a911-4b42-8e46-82d21f3fdab8` | ai | 0.839 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `6d2488cd-eb6e-4326-8ec1-8ffd0745f73f` | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `05811a2b-3c8e-46a4-bf9a-508a6c15763d` | ai | 0.944 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `28ff1c56-95a0-4e7c-8ebf-fd47dace95d5` | ai | 0.889 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `819c8c31-5ece-4a29-97a9-5c46b271f1c9` | unsure | 0.384 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `d439959b-d15e-481f-81e1-bc901186aae9` | human | 0.270 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1de0b9e6-4cf6-47f7-aeff-be83e30908eb` | human | 0.257 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d5f8e1f5-c344-4041-96e8-b660ec0c0149` | human | 0.257 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `716e1a7d-08d1-4bde-824b-19c5592a4127` | human | 0.257 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e77ef715-5847-4124-bc83-d77a41ad2f32` | human | 0.257 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3976901e-c2bc-4031-be2d-29b4b8fc7766` | human | 0.257 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7710e602-87da-4abb-8e13-6a7114f69520` | human | 0.257 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ec24bfc1-d181-4b22-814e-3a13d8d36264` | human | 0.257 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `60effce4-e2ed-445d-9131-7ac8b8c41719` | human | 0.257 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `90f93db9-069f-4678-8a91-04c844d793f7` | human | 0.257 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d34b02fb-f0de-44b6-86a2-ad39ecfc61ab` | human | 0.257 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 2 | 18 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "ad8261bd-f69c-428f-baab-1fcff372775c",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3202291265281521,
  "model_score": 0.1635,
  "style_score": 0.5553228163203803,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "1404d31c-f27c-45f9-9105-312234dac284",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4209112452732737,
  "model_score": 0.5943,
  "style_score": 0.16082811318318435,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "1a1f647a-dcbe-44fb-9deb-2854786b8296",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5589701004703447,
  "model_score": 0.6662,
  "style_score": 0.39812525117586145,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "23793373-eb12-478d-af8e-d6ef46c2c00d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5855377780081048,
  "model_score": 0.6114,
  "style_score": 0.5467444450202621,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "303f0f6e-ffb5-486a-858e-00aa4ff61526",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3077303235132824,
  "model_score": 0.3212,
  "style_score": 0.287525808783206,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "89356605-f250-482c-888f-c72c43995a9c",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.38361999999999996,
  "model_score": 0.5727,
  "style_score": 0.1,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "73c718e2-0a24-45dd-afa0-a2c10151dd35",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6280086597938145,
  "model_score": 0.5862,
  "style_score": 0.6907216494845361,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "f1b4464a-50a8-4c0d-a756-55244201d3e3",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3192377490060915,
  "model_score": 0.2452,
  "style_score": 0.43029437251522856,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "17af4700-f5d2-46f8-96a1-7427779e8b73",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5748157873671671,
  "model_score": 0.7042,
  "style_score": 0.38073946841791756,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "8dd449a1-d149-415c-8b77-58df66e3e3bf",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8417007702826427,
  "model_score": 0.9792,
  "style_score": 0.6354519257066069,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "9fddbb69-7402-4400-a639-d2eacbb2c793",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5473009176340347,
  "model_score": 0.6175,
  "style_score": 0.44200229408508673,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "96743b49-6a40-4b8d-9732-588ca55e4399",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6718519631207569,
  "model_score": 0.7387,
  "style_score": 0.571579907801892,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "1d8edbab-ac3f-47e5-b8b6-c9ab9c049690",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6886320184758965,
  "model_score": 0.8051,
  "style_score": 0.5139300461897411,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "5cffc596-0718-4d00-8573-96718d1cefc9",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6823251795794094,
  "model_score": 0.8329,
  "style_score": 0.45646294894852346,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "60766f03-62a5-4e88-a8c7-e5a6193b96ac",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7201327233823696,
  "model_score": 0.8005,
  "style_score": 0.5995818084559241,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "0a6c7c6c-7d2c-47fa-ae48-baec9fee0566",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6867406420562289,
  "model_score": 0.8814,
  "style_score": 0.3947516051405721,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "4ff30bde-d410-4fba-9180-152b4766dc22",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6803205994234229,
  "model_score": 0.8816,
  "style_score": 0.3784014985585573,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "75ebb1d1-4a1b-40cc-99b5-9716c43776c5",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.32945695154586735,
  "model_score": 0.3223,
  "style_score": 0.3401923788646684,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "7f733b76-f192-4158-b06f-80ff313ac386",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3691295640773652,
  "model_score": 0.4625,
  "style_score": 0.22907391019341297,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "5ad032fe-5f04-44df-a17a-8bb19ab44694",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.21331070712288305,
  "model_score": 0.2044,
  "style_score": 0.2266767678072076,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "a5875e1e-a799-409c-a604-2300703d59fb",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5287925283020515,
  "model_score": 0.5943,
  "style_score": 0.4305313207551286,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "8e6d9474-757c-493c-bdfa-72416baec445",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.46663142961258963,
  "model_score": 0.4998,
  "style_score": 0.41687857403147416,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "789ae7e7-7889-41a7-89c5-ac95146d0944",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5162562483434857,
  "model_score": 0.6401,
  "style_score": 0.3304906208587143,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "46494f60-baa7-4908-80fa-dda242790311",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5148018367291591,
  "model_score": 0.5583,
  "style_score": 0.449554591822898,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "a2bb6875-24e3-4639-9555-83b68d2985e6",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.24,
  "model_score": 0.0,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "4072aab1-a239-4e8f-afe7-a295de1f6659",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.40672,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "ffc22f94-a911-4b42-8e46-82d21f3fdab8",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.83856,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "6d2488cd-eb6e-4326-8ec1-8ffd0745f73f",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.99814,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "05811a2b-3c8e-46a4-bf9a-508a6c15763d",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.94384,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "28ff1c56-95a0-4e7c-8ebf-fd47dace95d5",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8887612478962414,
  "model_score": 0.9876,
  "style_score": 0.7405031197406038,
  "label": "We think this was probably generated by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "819c8c31-5ece-4a29-97a9-5c46b271f1c9",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.3837,
  "model_score": 0.2395,
  "style_score": 0.6,
  "label": "We are not confident enough to determine how this was written.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "d439959b-d15e-481f-81e1-bc901186aae9",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.26952,
  "model_score": 0.0492,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "1de0b9e6-4cf6-47f7-aeff-be83e30908eb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "d5f8e1f5-c344-4041-96e8-b660ec0c0149",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "716e1a7d-08d1-4bde-824b-19c5592a4127",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "e77ef715-5847-4124-bc83-d77a41ad2f32",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "3976901e-c2bc-4031-be2d-29b4b8fc7766",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "7710e602-87da-4abb-8e13-6a7114f69520",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "ec24bfc1-d181-4b22-814e-3a13d8d36264",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "60effce4-e2ed-445d-9131-7ac8b8c41719",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "90f93db9-069f-4678-8a91-04c844d793f7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d34b02fb-f0de-44b6-86a2-ad39ecfc61ab",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
