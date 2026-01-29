from fastapi import APIRouter, HTTPException
from app.schemas.symptom_schema import SymptomRequest, SymptomResponse
from app.services.symptom_ai import analyze_symptoms
from app.utils.hash_utils import generate_health_record_hash
from app.services.blockchain_service import store_hash_on_blockchain

router = APIRouter(prefix="/api", tags=["Symptoms"])

@router.post("/analyze", response_model=SymptomResponse)
def analyze(request: SymptomRequest):
    try:
        # 1. Call AI service
        ai_response = analyze_symptoms(request.text)

        # 2. Convert AI response to string (for hashing)
        ai_response_str = str(ai_response)

        # 3. Generate hash (privacy-safe)
        record_hash = generate_health_record_hash(
            symptoms=request.text,
            advice=ai_response_str
        )

        # 4. Store hash on blockchain (backend only)
        store_hash_on_blockchain(record_hash)

        # 5. Return AI response to frontend (unchanged)
        return ai_response

    except Exception as e:
        print("SYMPTOM AI ERROR:", e)
        raise HTTPException(
            status_code=503,
            detail="AI service temporarily unavailable"
        )
