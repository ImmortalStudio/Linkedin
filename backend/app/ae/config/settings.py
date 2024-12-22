"""
Settings configuration for Agent-E LinkedIn automation.
"""

import os
from typing import Optional

# Supabase Configuration
SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")

# LinkedIn Configuration
LINKEDIN_EMAIL: Optional[str] = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD: Optional[str] = os.getenv("LINKEDIN_PASSWORD")

# Agent Configuration
AUTOGEN_MODEL_NAME: str = os.getenv("AUTOGEN_MODEL_NAME", "gpt-4")
AUTOGEN_MODEL_API_KEY: str = os.getenv("AUTOGEN_MODEL_API_KEY", "")
AUTOGEN_MODEL_BASE_URL: Optional[str] = os.getenv("AUTOGEN_MODEL_BASE_URL")
AUTOGEN_MODEL_API_TYPE: str = os.getenv("AUTOGEN_MODEL_API_TYPE", "openai")
AUTOGEN_MODEL_API_VERSION: Optional[str] = os.getenv("AUTOGEN_MODEL_API_VERSION")

# Task Scheduling
MAX_CONCURRENT_TASKS: int = int(os.getenv("MAX_CONCURRENT_TASKS", "5"))
TASK_QUEUE_SIZE: int = int(os.getenv("TASK_QUEUE_SIZE", "100"))
