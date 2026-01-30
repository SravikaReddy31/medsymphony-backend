from pydantic import BaseModel
from typing import List

class FirstAidRequest(BaseModel):
    problem: str

class FirstAidResponse(BaseModel):
    steps: List[str]
    warning: str
