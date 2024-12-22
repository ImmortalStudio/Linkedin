"""
Agent-E package for LinkedIn automation.
"""
def get_click_using_selector():
    """Get click_using_selector function lazily."""
    from .core.skills.click_using_selector import click_using_selector
    return click_using_selector

def get_enter_text_and_click():
    """Get enter_text_and_click function lazily."""
    from .core.skills.enter_text_and_click import enter_text_and_click
    return enter_text_and_click

def get_open_url():
    """Get open_url function lazily."""
    from .core.skills.open_url import open_url
    return open_url

def get_get_url():
    """Get get_url function lazily."""
    from .core.skills.get_url import get_url
    return get_url

def get_enter_text_using_selector():
    """Get enter_text_using_selector function lazily."""
    from .core.skills.enter_text_using_selector import enter_text_using_selector
    return enter_text_using_selector

def get_autogen_wrapper():
    """Get AutogenWrapper class lazily."""
    from .core.autogen_wrapper import AutogenWrapper
    return AutogenWrapper

def get_system_orchestrator():
    """Get SystemOrchestrator class lazily."""
    from .core.system_orchestrator import SystemOrchestrator
    return SystemOrchestrator

def get_playwright_manager():
    """Get PlaywrightManager class lazily."""
    from .core.playwright_manager import PlaywrightManager
    return PlaywrightManager

def get_llm_config():
    """Get LLM configuration."""
    from .core.agents_llm_config import get_llm_config as _get_llm_config
    return _get_llm_config()

__all__ = [
    'get_autogen_wrapper',
    'get_system_orchestrator',
    'get_playwright_manager',
    'get_llm_config',
    'get_click_using_selector',
    'get_enter_text_and_click',
    'get_open_url',
    'get_get_url',
    'get_enter_text_using_selector'
]
