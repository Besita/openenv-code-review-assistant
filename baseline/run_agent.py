import os
import json
import re
import anthropic

from envs.code_review_env import CodeReviewEnv
from models.schema import Action

# Initialize Anthropic client
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


import json
import re

def parse_response(text):
    try:
        # 🔥 Step 1: Remove markdown wrappers like ```json ```
        text = re.sub(r"```.*?```", lambda m: m.group(0).strip("`"), text, flags=re.DOTALL)

        # 🔥 Step 2: Extract JSON object safely
        match = re.search(r"\{[\s\S]*?\}", text)

        if not match:
            raise ValueError("No JSON object found")

        clean_json = match.group(0)

        # 🔥 Step 3: Remove trailing commas (common LLM mistake)
        clean_json = re.sub(r",\s*}", "}", clean_json)
        clean_json = re.sub(r",\s*]", "]", clean_json)

        # 🔥 Step 4: Load JSON
        data = json.loads(clean_json)

        # 🔥 Ensure required fields exist
        data.setdefault("issues", [])
        data.setdefault("severity", "low")
        data.setdefault("suggestion", "")
        data.setdefault("reasoning", "")

        return Action(**data)

    except Exception as e:
        print("Parsing error:", e)
        print("Raw output:", text)

        return Action(
            issues=[],
            severity="low",
            suggestion="",
            reasoning=""
        )

def run():
    env = CodeReviewEnv()
    tasks = ["easy", "medium", "hard"]

    total_score = 0

    for t in tasks:
        print(f"\n🔹 Running task: {t}")

        obs = env.reset(t)

        prompt = f"""
            You are a senior software engineer performing a code review.

            Analyze the given code and return STRICT JSON in this format:

            Do NOT wrap the response in markdown.
            Do NOT use ```json or ```.

            {{
            "issues": ["..."],
            "severity": "low | medium | high",
            "suggestion": "...",
            "reasoning": "..."
            }}

            Rules:
            - Return ONLY valid JSON (no markdown, no ``` blocks)
            - Do NOT add any explanation before or after JSON
            - List ONLY the most important 1 or 2 issues
            - Ignore minor issues like:
            - docstrings
            - naming
            - formatting
            - style
            - Focus only on:
            - bugs
            - security issues
            - performance problems
            - Keep response concise and precise

            Code:
            {obs.code}
        """

        # Anthropic call
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        text_output = response.content[0].text

        print("LLM Output:", text_output)

        action = parse_response(text_output)
        # 🔥 Fix 2 Limit issues to top 2 (prevents penalty)
        # action.issues = action.issues[:2]
        important_keywords = ["injection", "zero", "loop", "performance"]

        filtered = [
            issue for issue in action.issues
            if any(k in issue.lower() for k in important_keywords)
        ]

        action.issues = (filtered or action.issues)[:2]

        _, reward, _, _ = env.step(action)

        print("Score:", reward.score)

        total_score += reward.score

    print("\n===================")
    print("Final Score:", total_score / len(tasks))


if __name__ == "__main__":
    run()