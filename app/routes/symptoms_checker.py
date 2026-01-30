from fastapi import APIRouter, HTTPException
from app.schemas.symptom_schema import SymptomRequest, SymptomResponse
from app.services.symptom_ai import analyze_symptoms

router = APIRouter()

@router.post("/analyze", response_model=SymptomResponse)
def analyze(request: SymptomRequest):
    try:
        return analyze_symptoms(request.text)
    except Exception as e:
        print("SYMPTOM AI ERROR:", e)
        raise HTTPException(
            status_code=503,
            detail="AI service temporarily unavailable"
        )
