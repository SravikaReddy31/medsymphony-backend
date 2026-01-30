from fastapi import APIRouter, HTTPException
from app.schemas.first_aid_schema import FirstAidRequest, FirstAidResponse
from app.services.first_aid_ai import generate_first_aid

router = APIRouter()

@router.post("/analyze", response_model=FirstAidResponse)
def first_aid_api(request: FirstAidRequest):
    try:
        return generate_first_aid(request.problem)
    except Exception as e:
        print("FIRST AID API ERROR:", e)
        raise HTTPException(
            status_code=503,
            detail="AI service temporarily unavailable"
        )
