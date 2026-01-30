import json
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_symptoms(user_input: str):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a medical symptom analysis assistant.\n\n"
                        "LANGUAGE RULE:\n"
                        "- If user writes in Telugu → reply only in SIMPLE TELUGU\n"
                        "- If user writes in English → reply only in SIMPLE ENGLISH\n"
                        "- Do not mix languages\n\n"
                        "OUTPUT RULES:\n"
                        "- Reply ONLY in valid JSON\n"
                        "- No explanation outside JSON\n"
                        "- Use very simple words\n"
                        "- Avoid complex medical terms\n\n"
                        "FORMAT:\n"
                        "{\n"
                        '  "urgency": "",\n'
                        '  "possible_condition": "",\n'
                        '  "food_advice": [],\n'
                        '  "exercise_advice": [],\n'
                        '  "pain_relief": [],\n'
                        '  "disclaimer": ""\n'
                        "}"
                    )
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()

        return json.loads(content)

    except Exception as e:
        print("GROQ ERROR:", e)
        return {
            "urgency": "medium",
            "possible_condition": "General health issue",
            "food_advice": ["Drink water", "Eat light food"],
            "exercise_advice": [],
            "pain_relief": ["Take rest"],
            "disclaimer": "Please consult a doctor if symptoms continue."
        }
