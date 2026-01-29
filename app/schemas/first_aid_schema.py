from pydantic import BaseModel
class FirstAidRequest(BaseModel):
    problem: str
class FirstAidResponse(BaseModel):
    result: str
