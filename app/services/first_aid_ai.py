import json
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_first_aid(user_input: str):
    messages = [
        {
            "role": "system",
            "content": """
You are a FIRST AID assistant.

RULES:
- If user writes in Telugu → reply only in SIMPLE TELUGU
- If user writes in English → reply only in SIMPLE ENGLISH
- Do not mix languages

OUTPUT:
- Reply ONLY in valid JSON
- Keep steps very simple

FORMAT:
{
  "steps": [],
  "warning": ""
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
            "steps": data.get("steps", []),
            "warning": data.get(
                "warning",
                "Consult a doctor if condition worsens."
            )
        }

    except Exception as e:
        print("FIRST AID GROQ ERROR:", e)

        return {
            "steps": ["Please rest and seek medical help"],
            "warning": "Consult a doctor if condition worsens."
        }
