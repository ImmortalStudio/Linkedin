"""
Agent-E package for LinkedIn automation.
"""
from .core import get_autogen_wrapper, get_system_orchestrator, get_playwright_manager, get_llm_config
from .core.skills import click_using_selector, enter_text_and_click, open_url, get_url, enter_text_using_selector

# Initialize classes lazily to avoid circular imports
AutogenWrapper = get_autogen_wrapper()
SystemOrchestrator = get_system_orchestrator()
PlaywrightManager = get_playwright_manager()

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
