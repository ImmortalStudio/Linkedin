"""
DOM manipulation and querying utilities for Agent-E LinkedIn automation.
"""

from typing import Optional, Dict, Any, List

def extract_element_info(element: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract relevant information from a DOM element.
    
    Args:
        element: Dictionary containing element information
        
    Returns:
        Dict containing processed element information
    """
    return {
        'tag': element.get('tagName', '').lower(),
        'text': element.get('textContent', ''),
        'attributes': element.get('attributes', {}),
        'classes': element.get('className', '').split(),
        'id': element.get('id', '')
    }

def find_clickable_elements(dom_tree: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Find all clickable elements in the DOM tree.
    
    Args:
        dom_tree: Dictionary representing the DOM tree
        
    Returns:
        List of clickable elements with their information
    """
    clickable = []
    
    def is_clickable(element: Dict[str, Any]) -> bool:
        tag = element.get('tagName', '').lower()
        role = element.get('attributes', {}).get('role', '')
        
        return (
            tag in ['button', 'a', 'input'] or
            role in ['button', 'link'] or
            'click' in str(element.get('listeners', []))
        )
    
    def traverse(node: Dict[str, Any]):
        if is_clickable(node):
            clickable.append(extract_element_info(node))
            
        for child in node.get('children', []):
            traverse(child)
    
    traverse(dom_tree)
    return clickable


def find_input_elements(dom_tree: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Find all input elements in the DOM tree.
    
    Args:
        dom_tree: Dictionary representing the DOM tree
        
    Returns:
        List of input elements with their information
    """
    inputs = []
    
    def is_input(element: Dict[str, Any]) -> bool:
        tag = element.get('tagName', '').lower()
        role = element.get('attributes', {}).get('role', '')
        
        return (
            tag in ['input', 'textarea'] or
            role in ['textbox', 'searchbox']
        )
    
    def traverse(node: Dict[str, Any]):
        if is_input(node):
            inputs.append(extract_element_info(node))
            
        for child in node.get('children', []):
            traverse(child)
    
    traverse(dom_tree)
    return inputs
