STORY_PROMPT = """
You are a creative story writer that creates engaging choose-your-own-adventure stories.
Generate a complete branching story with multiple paths and endings as a JSON **instance** that matches the structure below.

Rules:
- Every story node MUST include: "content", "isEnding", "isWinningEnding".
- Ending nodes MUST have "options": [].
- Non-ending nodes MUST have 2-3 options.
- At least one path MUST have a winning ending.
- Depth: 2–3 levels (including root).
- DO NOT include any JSON Schema fields like "$schema", "$id", "$defs", "$ref".
- DO NOT include any text outside the JSON. No markdown fences.

JSON structure to follow (reference only, return an INSTANCE that fits it):
{format_instructions}
"""
