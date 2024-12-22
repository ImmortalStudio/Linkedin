import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .routers import linkedin
from .database import verify_supabase_connection, get_supabase

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LinkedIn Automation API")

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    """Verify all connections and configurations on startup."""
    try:
        logger.info("Verifying Supabase connection...")
        await verify_supabase_connection()
        logger.info("Supabase connection verified successfully")
    except Exception as e:
        logger.error(f"Failed to verify Supabase connection: {str(e)}")
        raise

@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error", "error": str(e)}
        )

# Include routers
app.include_router(linkedin.router, prefix="/api/linkedin", tags=["linkedin"])

@app.get("/healthz")
async def healthz():
    """Health check endpoint that verifies Supabase connection."""
    try:
        await verify_supabase_connection()
        return {
            "status": "ok",
            "supabase": "connected"
        }
    except Exception as e:
        return {
            "status": "error",
            "supabase": str(e)
        }

@app.get("/")
def read_root():
    return {
        "name": "LinkedIn Automation API",
        "version": "1.0.0",
        "description": "API for LinkedIn outreach automation and BDR scheduling"
    }
