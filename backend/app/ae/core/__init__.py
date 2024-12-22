"""Core functionality for Agent-E."""
from .agents_llm_config import get_llm_config

__all__ = ['get_llm_config']

def get_autogen_wrapper():
    """Get AutogenWrapper class lazily to avoid circular imports."""
    from .autogen_wrapper import AutogenWrapper
    return AutogenWrapper

def get_system_orchestrator():
    """Get SystemOrchestrator class lazily to avoid circular imports."""
    from .system_orchestrator import SystemOrchestrator
    return SystemOrchestrator

def get_playwright_manager():
    """Get PlaywrightManager class lazily to avoid circular imports."""
    from .playwright_manager import PlaywrightManager
    return PlaywrightManager
