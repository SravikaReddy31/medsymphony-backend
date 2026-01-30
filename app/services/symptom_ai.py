import json
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_symptoms(user_input: str):
    messages = [
        {
            "role": "system",
            "content": """
You are a medical symptom analysis assistant.

LANGUAGE RULE:
- If user writes in Telugu → reply only in SIMPLE TELUGU
- If user writes in English → reply only in SIMPLE ENGLISH
- Do not mix languages

OUTPUT RULES:
- Reply ONLY in valid JSON
- No explanation outside JSON
- Use very simple words
- Avoid complex medical terms

FORMAT:
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
            model="llama3-8b-8192",   # ✅ SAFE MODEL
            messages=messages,
            temperature=0.2
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except Exception:
            return {
                "urgency": "medium",
                "possible_condition": "General health issue",
                "food_advice": [],
                "exercise_advice": [],
                "pain_relief": [],
                "disclaimer": "Please consult a doctor if symptoms continue."
            }

    except Exception as e:
        print("GROQ ERROR:", e)
        raise Exception("AI service temporarily unavailable")
