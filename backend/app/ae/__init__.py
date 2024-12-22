"""
Agent-E package for LinkedIn automation.
"""
# Import core modules directly to avoid circular imports
from .core.autogen_wrapper import AutogenWrapper
from .core.system_orchestrator import SystemOrchestrator
from .core.playwright_manager import PlaywrightManager
from .core.agents_llm_config import get_llm_config
from .core.skills import (
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
