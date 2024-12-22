"""
Agent-E package for LinkedIn automation.
"""
from . import core

# Re-export core components
AutogenWrapper = core.AutogenWrapper
SystemOrchestrator = core.SystemOrchestrator
PlaywrightManager = core.PlaywrightManager
get_llm_config = core.get_llm_config
click_using_selector = core.click_using_selector
enter_text_and_click = core.enter_text_and_click
open_url = core.open_url
get_url = core.get_url
enter_text_using_selector = core.enter_text_using_selector

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
