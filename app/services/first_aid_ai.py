import json
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_first_aid_advice(user_input: str):
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
            model="llama3-8b-8192",
            messages=messages,
            temperature=0.2
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        print("FIRST AID GROQ ERROR:", e)
        return {
            "steps": ["Please rest and seek medical help"],
            "warning": "Consult a doctor if condition worsens"
        }
