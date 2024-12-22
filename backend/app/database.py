from typing import AsyncGenerator
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials in environment variables")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

async def get_supabase() -> AsyncGenerator[Client, None]:
    try:
        yield supabase
    finally:
        pass  # Connection management handled by Supabase client
