import json
from openai import OpenAI, OpenAIError
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def analyze_symptoms(user_input: str):
    messages = [
        {
            "role": "system",
            "content": """
You are a medical symptom analysis assistant.

VERY IMPORTANT LANGUAGE RULE:
- If the user's input is in Telugu, respond ONLY in SIMPLE TELUGU.
- If the user's input is in English, respond ONLY in SIMPLE ENGLISH.
- Do NOT mix languages.

IMPORTANT OUTPUT RULES:
- Respond ONLY in valid JSON.
- Do NOT explain anything outside JSON.
- Always fill ALL fields.
- Use very simple words suitable for common people.
- Avoid complex medical terms.

FORMAT (must be exactly this):
{
  "urgency": "",
  "possible_condition": "",
  "food_advice": [],
  "exercise_advice": [],
  "pain_relief": [],
  "disclaimer": ""
}
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.2,
            timeout=30
        )

        content = response.choices[0].message.content.strip()
        return json.loads(content)

    except OpenAIError:
        # Honest failure
        raise Exception("AI is temporarily unavailable. Please try again.")

    except Exception:
        raise Exception("Unable to process symptoms right now. Please retry.")
