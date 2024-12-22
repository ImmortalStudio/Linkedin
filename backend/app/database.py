import logging
from typing import AsyncGenerator
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from postgrest import APIError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials in environment variables")

try:
    logger.info("Initializing Supabase client...")
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    logger.info("Supabase client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Supabase client: {str(e)}")
    raise

async def verify_supabase_connection() -> bool:
    """Verify Supabase connection by making a test query."""
    try:
        # Try to fetch a single row from any table to verify connection
        await supabase.table('campaigns').select("*").limit(1).execute()
        return True
    except APIError as e:
        logger.error(f"Supabase connection test failed: {str(e)}")
        raise Exception(f"Failed to connect to Supabase: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error during Supabase connection test: {str(e)}")
        raise

async def get_supabase() -> AsyncGenerator[Client, None]:
    """Get Supabase client with connection verification."""
    try:
        await verify_supabase_connection()
        yield supabase
    except Exception as e:
        logger.error(f"Error in Supabase client: {str(e)}")
        raise
    finally:
        pass  # Connection management handled by Supabase client
