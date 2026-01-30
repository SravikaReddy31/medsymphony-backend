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
- Steps should be easy for common people
- Avoid medical jargon
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
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()
        return json.loads(content)

    except Exception as e:
        print("GROQ FIRST AID ERROR:", e)
        raise Exception("AI service temporarily unavailable")
