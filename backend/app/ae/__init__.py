"""
Agent-E package for LinkedIn automation.
"""

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
    'get_llm_config'
]
