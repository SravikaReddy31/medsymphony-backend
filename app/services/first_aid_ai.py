from openai import OpenAI
from app.config import settings   # where API key is stored

# Create OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_first_aid(user_input: str):
    messages = [
        {
            "role": "system",
            "content": """
You are a first aid medical assistant.

The user input may be in English or Telugu.
If the input is in English, respond ONLY in English.
If the input is in Telugu, respond ONLY in Telugu.
Do NOT mix languages.

TASK:
- Identify the problem.
- Mention urgency level (Normal / Moderate / Emergency).
- Give simple first aid guidance.
- Mention when to go to a hospital.

Do NOT prescribe medicines.
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content
