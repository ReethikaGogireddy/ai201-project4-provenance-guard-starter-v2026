"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "The sun, the moon come everyday to tell me that they will be with me at every part of my time.",
            "The sun is so beautiful during the sunset.",
            "The moon is so beautiful that I can't stop myself from seeing it.",
            "I like to walk, when I am thinking for any ideas.",
            "Studying is a so fun sometimes.",
            "Learning everything in this era, is the most common thing right now.",
            "The world is so silent at night and in the morning.",
            "Doom scrolling is new productivity I guess.",
            "I am starting to fall in love with the art of writing.",
            "Health is the real wealth.",
        ],
    },

    {
        "name": "AI and human score difference",
        "criterion": 2,
        "texts": [
            # Human-generated
            """Many people think that styding is a waste of time, but I think that
            is the most important thing. When we study we will know all the
            inventions or discoveries that happened and we can focus on solving
            new problem.""",

            # AI-generated
            """Studying helps people gain knowledge, develop useful skills, and
            better understand the world around them. It also strengthens abilities
            such as critical thinking, problem-solving, and communication, which
            are valuable in both personal and professional life. Education can
            create new opportunities and help people make more informed decisions.
            Ultimately, studying is not only about earning good grades but also
            about developing the knowledge and skills needed for the future.""",
        ],
    },

    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            # Clearly AI-generated
            """Studying helps people gain knowledge, develop useful skills, and better
            understand the world around them. It also strengthens abilities such as
            critical thinking, problem-solving, and communication, which are valuable
            in both personal and professional life. Education can create new
            opportunities and help people make more informed decisions.""",

            # Clearly human-written
            """Studying will help us understand the world around us. How did we evolve,
            why did we evolve. How things changed, how they actually effected us.
            We will learn to understand the world, body, enviroment and more.""",

            # Borderline — lightly edited AI-generated text
            """Studying helps us learn new things and understand things better.
            It can also help with problem solving and communication. But everyone
            studies differently, and sometimes learning from experience can be just
            as useful as learning from books."""
        ],
    },

    {
        "name": "missing or empty text",
        "criterion": 5,
        "bodies": [
            {
                "text": "",
                "creator_id": "eval_bad_empty"
            },
            {
                "creator_id": "eval_bad_missing"
            },
        ],
    },

    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    # {
    #     "name": "bad input",
    #     "criterion": 3,
    #     "bodies": [
    #         {"text": "", "creator_id": "eval_bad_empty"},
    #         {"creator_id": "eval_bad_missing"},          # no text field at all
    #         {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
    #         {"text": None, "creator_id": "eval_bad_null"},
    #     ],
    # },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems