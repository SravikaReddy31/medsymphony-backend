from pydantic import BaseModel
from typing import List

class SymptomRequest(BaseModel):
    text: str

class SymptomResponse(BaseModel):
    urgency: str
    possible_condition: str
    food_advice: List[str]
    exercise_advice: List[str]
    pain_relief: List[str]
    disclaimer: str
