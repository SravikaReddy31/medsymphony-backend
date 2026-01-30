import json
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_first_aid(user_input: str):
    messages = [
        {
            "role": "system",
            "content": """
You are a first aid assistant.

LANGUAGE RULE:
- If user writes in Telugu → reply only in SIMPLE TELUGU
- If user writes in English → reply only in SIMPLE ENGLISH
- Do not mix languages

RULES:
- Use very simple words
- Steps must be easy for common people
- Avoid medical terms
- Respond ONLY in valid JSON

FORMAT:
{
  "emergency": "",
  "steps": [],
  "do_not_do": [],
  "when_to_go_hospital": "",
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
            model="llama3-70b-8192",
            messages=messages,
            temperature=0.2,
            max_tokens=600
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except Exception:
            # Fallback if AI response is not valid JSON
            return {
                "emergency": "Possible emergency",
                "steps": [
                    "Stay calm",
                    "Help the person sit or lie down",
                    "Do not panic"
                ],
                "do_not_do": [
                    "Do not give random medicines",
                    "Do not ignore symptoms"
                ],
                "when_to_go_hospital": "If pain or problem continues",
                "disclaimer": "This is basic first aid advice. Please consult a doctor."
            }

    except Exception as e:
        print("GROQ FIRST AID ERROR:", e)
        raise Exception("AI service temporarily unavailable")
