"""Web interaction skills for Agent-E."""

def get_click_using_selector():
    """Get click_using_selector function lazily."""
    from .click_using_selector import click_using_selector
    return click_using_selector

def get_enter_text_and_click():
    """Get enter_text_and_click function lazily."""
    from .enter_text_and_click import enter_text_and_click
    return enter_text_and_click

def get_open_url():
    """Get open_url function lazily."""
    from .open_url import open_url
    return open_url

def get_get_url():
    """Get get_url function lazily."""
    from .get_url import get_url
    return get_url

def get_enter_text_using_selector():
    """Get enter_text_using_selector function lazily."""
    from .enter_text_using_selector import enter_text_using_selector
    return enter_text_using_selector

__all__ = [
    'get_click_using_selector',
    'get_enter_text_and_click',
    'get_open_url',
    'get_get_url',
    'get_enter_text_using_selector'
]
