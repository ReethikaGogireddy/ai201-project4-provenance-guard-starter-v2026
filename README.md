# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->


1. A writer submits their text and creator ID through the `POST /submit` endpoint.
2. `detector.py` analyzes the text using the local model and produces the model signal score.
3. `stylometry.py` analyzes writing characteristics such as sentence length, word variety, and punctuation and produces the style signal score.
4. `scoring.py::combine_signals` combines the two signal scores into one confidence score.
5. `scoring.py::score_to_label` maps the confidence score to one of three labels: high-confidence AI, high-confidence human, or unsure.
6. `audit.py` records the submission, signal scores, decision, and status in the audit log.
7. The `/submit` endpoint returns the content ID, guess, confidence score, signal scores, and reader-facing label as JSON.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
It uses a local model to analyze the text and produce a score based on how predictable the writing is.

**Why that might differ between human and AI writing:**
AI-generated text may be more predictable because language models generate text based on likely word patterns.

**What it can't see:**
Human writing can be predictable, but edited AI writing can appear less predictable.

### Signal two — the style signal

**What it measures:**
It measures writing features such as sentence-length variation, word variety, and punctuation.

**Why that might differ between human and AI writing:**
Human and AI writing may have different patterns in sentence structure, vocabulary, and punctuation.

**What it can't see:**
It cannot determine authorship from style alone. A human and an AI can produce similar writing patterns. Since, gpt are also trained on human writing it's style may not be completely different from the human.

**False-positive trace:**

Human submits real writing → /submit receives it → model and style signals analyze it → combined score incorrectly leans toward AI → writer sees the AI label → writer disagrees → writer submits an appeal → content status changes to under_review.

### Endpoint 1 — POST /submit

**Input:**
```json
{
  "text": "The writing submitted by the user",
  "creator_id": "user123"
}
```

**Output:**
```json
{
  "content_id": "content123",
  "guess": "human or AI",
  "confidence": 0.0,
  "label": "reader-facing label",
  "model_score": 0.0,
  "style_score": 0.0
}
```

`text` contains the writing to analyze, and `creator_id` identifies the writer. The response gives the submission an ID and returns the system's guess, confidence, label, and the two signal scores.


### Endpoint 2 — POST /appeal

**Input:**
```json
{
  "content_id": "content123",
  "reasoning": "Why the writer thinks the decision is incorrect"
}
```

**Output:**
```text
Confirmation that the appeal was recorded
Status: under_review
```

`content_id` identifies the original submission, and the reasoning explains why the writer disagrees with the decision. The appeal is recorded and the item's status changes to `under_review`.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

I use a weighted average of the model signal and the style signal. I give the model signal more weight because my testing showed that the style signal did not separate human and AI writing as clearly. When the two signals disagree, the combined score moves toward the middle to represent the uncertainty.

**The numbers:**

Model signal: 60%
Style signal: 40%

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

For one AI-generated machine learning sample, the model signal was `0.6058`, while the style signal was `0.4503`. Using my 60% model and 40% style weighting, the combined score was `0.5436`. Since the two signals differed, the weighted combination moved the final score toward the middle, representing uncertainty rather than relying completely on either signal.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | > 0.35 and < 0.65 | We are not confident enough to determine how this was written. |
| high-confidence AI | 0.65 – 1.00 | We think this was probably generated by AI. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

I wanted the label to clearly communicate that the system is uncertain without accusing the writer of using AI.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"Machine learning allows computers to identify patterns in data and make predictions. Models improve their performance by learning from examples.","creator_id":"user1"}'
```

```json
{
  "confidence": 0.5435977490060915,
  "content_id": "16648482-ff26-4b72-a521-d6459bb8c1d4",
  "guess": "unsure",
  "label": "We are not confident enough to determine how this was written.",
  "model_score": 0.6058,
  "style_score": 0.4502943725152286
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"16648482-ff26-4b72-a521-d6459bb8c1d4","reasoning":"I wrote this text myself."}'
```

```json

{
  "content_id": "16648482-ff26-4b72-a521-d6459bb8c1d4",
  "message": "Your appeal has been recorded.",
  "status": "under_review"
}

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.5435977490060915,
      "content_id": "a7bb5fbe-c02e-4afc-8839-daaf83c2a083",
      "creator_id": "user1",
      "guess": "placeholder",
      "label": "placeholder",
      "model_score": 0.6058,
      "status": "decided",
      "style_score": 0.4502943725152286,
      "timestamp": "2026-11-04T01:45:35+00:00"
    },
    {
      "combined_score": 0.5435977490060915,
      "content_id": "16648482-ff26-4b72-a521-d6459bb8c1d4",
      "creator_id": "user1",
      "guess": "unsure",
      "label": "We are not confident enough to determine how this was written.",
      "model_score": 0.6058,
      "status": "decided",
      "style_score": 0.4502943725152286,
      "timestamp": "2026-11-04T01:59:08+00:00"
    },
    {
      "content_id": "16648482-ff26-4b72-a521-d6459bb8c1d4",
      "creator_id": "user1",
      "event": "appeal",
      "reasoning": "I wrote this text myself.",
      "status": "under_review",
      "timestamp": "2026-11-04T02:03:44+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*  I asked AI for help understanding how to build and combine the stylometry features for the second signal.
- *What came back:* AI suggested measuring sentence-length variation, vocabulary variety, and punctuation density and explained how they could be converted into a style score.
- *What I changed:* I tested the features on human, AI-generated, and edited AI text. Based on my results, I adjusted the weights and used a 60% model signal and 40% style signal for the final combined score.

**Moment 2**

- *What I asked for:* I asked AI why my /submit endpoint was giving an UnboundLocalError for confidence.
- *What came back:* AI pointed out that I was calling score_to_label(confidence) before calculating confidence.
- *What I changed:* I moved score_to_label() after combine_signals(), then tested /submit again and confirmed that it returned the correct guess and label.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day
python run_attacks.py --flood 15

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

I chose 10 requests per minute because it allows a normal writer to submit several pieces of writing without being blocked, while limiting scripts that send many requests quickly. The 200-per-day limit also prevents a single caller from continuously submitting large numbers of requests.

**What a caller counts as:** <!-- per address, or per creator_id? They fail differently — one script can look like a thousand callers, and one household
can look like one. -->
A caller is identified by creator_id. If a valid creator_id is not available, the caller's address is used instead.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---:|---|---:|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.320 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.421 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.559 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.586 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.308 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.384 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.628 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.319 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.575 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.842 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.547 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.672 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.689 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.682 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.720 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.687 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.680 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | human | 0.329 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.369 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.213 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.529 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.467 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.516 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.515 | HELD |
| MF01 | malformed | text is only whitespace | 200 | unsure | 0.523 | BROKE |
| MF02 | malformed | text is a single character | 500 | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | human | 0.240 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.407 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.839 | BROKE |
| MF06 | malformed | text is emoji only | 200 | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.944 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | ai | 0.889 | BROKE |
| RQ01 | malformed | no text field at all | 500 | — | — | BROKE |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.384 | BROKE |
| RQ03 | malformed | text is a number | 500 | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.270 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 500 | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 500 | — | — | BROKE |
| RQ09 | malformed | body is empty | 500 | — | — | BROKE |
| RQ10 | malformed | body is form-encoded, not JSON | 500 | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 500 | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 500 | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```jsons
[
  {
    "combined_score": 0.3202291265281521,
    "content_id": "4cd89a5f-a163-40ca-821a-c22c83a2046a",
    "creator_id": "attacker_EV01",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.1635,
    "status": "decided",
    "style_score": 0.5553228163203803,
    "timestamp": "2026-11-11T05:31:28+00:00"
  },
  {
    "combined_score": 0.5589701004703447,
    "content_id": "0edc7166-c752-4e65-8df8-64dc0071803f",
    "creator_id": "attacker_EV03",
    "guess": "unsure",
    "label": "We are not confident enough to determine how this was written.",
    "model_score": 0.6662,
    "status": "decided",
    "style_score": 0.39812525117586145,
    "timestamp": "2026-11-11T05:31:28+00:00"
  },
  {
    "combined_score": 0.8417007702826427,
    "content_id": "d6e4dff7-27b7-44e4-938b-2c83ba976f1e",
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "label": "We think this was probably generated by AI.",
    "model_score": 0.9792,
    "status": "decided",
    "style_score": 0.6354519257066069,
    "timestamp": "2026-11-11T05:31:29+00:00"
  },
  {
    "combined_score": 0.6718519631207569,
    "content_id": "27ed7352-47d0-4c5c-9322-ea11338a6432",
    "creator_id": "attacker_FP02",
    "guess": "ai",
    "label": "We think this was probably generated by AI.",
    "model_score": 0.7387,
    "status": "decided",
    "style_score": 0.571579907801892,
    "timestamp": "2026-11-11T05:31:29+00:00"
  },
  {
    "combined_score": 0.7201327233823696,
    "content_id": "8a8c9384-2065-4ac4-b4dc-7ccd605ae418",
    "creator_id": "attacker_FP05",
    "guess": "ai",
    "label": "We think this was probably generated by AI.",
    "model_score": 0.8005,
    "status": "decided",
    "style_score": 0.5995818084559241,
    "timestamp": "2026-11-11T05:31:29+00:00"
  },
  {
    "combined_score": 0.21331070712288305,
    "content_id": "5d9ba8b7-c94f-4cd9-99c2-50d884915f14",
    "creator_id": "attacker_PI02",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.2044,
    "status": "decided",
    "style_score": 0.2266767678072076,
    "timestamp": "2026-11-11T05:31:29+00:00"
  },
  {
    "combined_score": 0.52318,
    "content_id": "1cb9ebbb-9463-4c58-b166-ed6a4ebaeac5",
    "creator_id": "attacker_MF01",
    "guess": "unsure",
    "label": "We are not confident enough to determine how this was written.",
    "model_score": 0.2053,
    "status": "decided",
    "style_score": 1.0,
    "timestamp": "2026-11-11T05:31:29+00:00"
  },
  {
    "combined_score": 0.99814,
    "content_id": "a31ae6f6-5786-40bb-bc52-319c667127c6",
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "label": "We think this was probably generated by AI.",
    "model_score": 0.9969,
    "status": "decided",
    "style_score": 1.0,
    "timestamp": "2026-11-11T05:31:30+00:00"
  },
  {
    "combined_score": 0.25722,
    "content_id": "056352d3-8acc-485f-8b17-6de4b449da2d",
    "creator_id": "attacker_flood",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.0287,
    "status": "decided",
    "style_score": 0.6,
    "timestamp": "2026-11-11T05:31:30+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-11T05:31:30+00:00"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP05 was the worst outcome because technical documentation written by a person was labeled as AI with a confidence score of 0.7201. I would least want to explain this result to a real writer because the system confidently accused human-written work of being AI-generated.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

## Run Log and Verdicts

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing | At most 2 of 10 labeled high-confidence AI | 2/10 AI | 2/10 AI | 2/10 AI | MET |
| 2. AI and human score difference | Confidence-score difference ≥ 0.70 | 0.022 | 0.022 | 0.022 | MISSED |
| 3. Label coverage | All 3 labels reachable | 1/3 labels | 1/3 labels | 1/3 labels | MISSED |
| 4. Appeal path | 100% of valid appeals recorded and changed to `under_review` | 1/1 | 1/1 | 1/1 | MET |
| 5. Missing or empty text | 100% rejected without crashing | 0/2 | 0/2 | 0/2 | MISSED |

**Real output from one trial**, produced by `run_eval.py::main` using the Criterion 2 scenario from `scenarios.py`:

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7421294372515228,
    "model_score": 0.8185,
    "style_score": 0.6275735931288072,
    "label": "We think this was probably generated by AI.",
    "sent": "Many people think that styding is a waste of time, but I think that\n  "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7641773913043478,
    "model_score": 0.9316,
    "style_score": 0.5130434782608695,
    "label": "We think this was probably generated by AI.",
    "sent": "Studying helps people gain knowledge, develop useful skills, and\n     "
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

Criterion 2 — MISSED  
Stage: Signal one / combining rule.  
Mechanism: The human and AI samples both received high model scores, so their final scores were only 0.022 apart instead of 0.70.

Criterion 3 — MISSED  
Stage: Signal one / label mapping.  
Mechanism: All three inputs scored above the 0.65 AI threshold, so only the AI label was reached.

Criterion 5 — MISSED  
Stage: Route.  
Mechanism: Missing and empty text were not validated before scoring, causing errors instead of safe rejections.

Evasion attacks  
Stage: Signals one and two.  
Mechanism: Changes to vocabulary, sentence structure, and punctuation lowered the scores, allowing AI text to be labeled human or unsure.

False-positive attacks  
Stage: Signal one / combining rule.  
Mechanism: Human writing received high model scores, and the 60% model weight pushed several results above the AI threshold.

Malformed-input attacks  
Stage: Route.  
Mechanism: Invalid inputs were not validated before scoring, causing some to be accepted and others to crash with 500 errors.

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
