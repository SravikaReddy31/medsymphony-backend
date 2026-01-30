from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.symptoms_checker import router as symptom_router
from app.routes.first_aid import router as first_aid_router

app = FastAPI(title="MedSymphony API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://medsymphony.in",
        "https://www.medsymphony.in"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(symptom_router, prefix="/symptoms", tags=["Symptoms"])
app.include_router(first_aid_router, prefix="/first-aid", tags=["First Aid"])
