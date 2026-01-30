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

RULES:
- If user writes in Telugu → reply only in SIMPLE TELUGU
- If user writes in English → reply only in SIMPLE ENGLISH
- Do not mix languages

OUTPUT:
- Reply ONLY in valid JSON
- food_advice, exercise_advice, pain_relief MUST be arrays

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
            model="llama3-8b-8192",
            messages=messages,
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()
        data = json.loads(content)

        return {
            "urgency": data.get("urgency", "medium"),
            "possible_condition": data.get(
                "possible_condition", "General health issue"
            ),
            "food_advice": data.get("food_advice", []),
            "exercise_advice": data.get("exercise_advice", []),
            "pain_relief": data.get("pain_relief", []),
            "disclaimer": data.get(
                "disclaimer",
                "Please consult a doctor if symptoms continue."
            )
        }

    except Exception as e:
        print("GROQ ERROR:", e)

        return {
            "urgency": "medium",
            "possible_condition": "General health issue",
            "food_advice": [],
            "exercise_advice": [],
            "pain_relief": [],
            "disclaimer": "Please consult a doctor if symptoms continue."
        }
