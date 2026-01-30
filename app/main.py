from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.symptoms_checker import router as symptoms_router
from app.routes.first_aid import router as first_aid_router
from app.routes.hospitals import router as hospitals_router

app = FastAPI(
    title="MedSymphony Backend",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 🔥 CORS MUST BE FIRST (before routers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://medsymphony.in",
        "https://www.medsymphony.in",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# ✅ Routers
app.include_router(symptoms_router, prefix="/api")
app.include_router(first_aid_router, prefix="/api")
app.include_router(hospitals_router, prefix="/api")
