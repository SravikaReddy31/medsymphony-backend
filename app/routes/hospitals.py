from fastapi import APIRouter
from app.services.hospitals_data import hospitals

router = APIRouter(prefix="/api", tags=["Hospitals"])

@router.get("/hospitals")
def get_hospitals():
    return hospitals   # ✅ RETURN LIST DIRECTLY
