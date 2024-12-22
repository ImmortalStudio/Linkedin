"""Core functionality for Agent-E."""
# Import core modules directly to avoid circular imports
from .autogen_wrapper import AutogenWrapper
from .system_orchestrator import SystemOrchestrator
from .playwright_manager import PlaywrightManager
from .agents_llm_config import get_llm_config
from .skills import (
    click_using_selector,
    enter_text_and_click,
    open_url,
    get_url,
    enter_text_using_selector
)

__all__ = [
    'AutogenWrapper',
    'SystemOrchestrator',
    'PlaywrightManager',
    'get_llm_config',
    'click_using_selector',
    'enter_text_and_click',
    'open_url',
    'get_url',
    'enter_text_using_selector'
]
