from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.incidents import router as incidents_router


app = FastAPI(
    title="SAFEHOLD API",
    description="Privacy-first safety and support platform",
    version="0.2.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    auth_router,
    prefix="/api",
)

app.include_router(
    incidents_router,
    prefix="/api",
)


@app.get("/")
def root():
    return {
        "name": "SAFEHOLD",
        "message": "SAFEHOLD API is running.",
        "version": "0.2.0",
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SAFEHOLD API",
    }
