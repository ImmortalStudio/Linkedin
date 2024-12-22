from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import linkedin

app = FastAPI(title="LinkedIn Automation API")

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(linkedin.router, prefix="/api/linkedin", tags=["linkedin"])

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {
        "name": "LinkedIn Automation API",
        "version": "1.0.0",
        "description": "API for LinkedIn outreach automation and BDR scheduling"
    }
