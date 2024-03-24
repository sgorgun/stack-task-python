"""Template for programming assignment: parentheses validation."""
from tasks.stack import Stack, LinkedListNode

def is_valid_parentheses(expression: str) -> bool:
    """Returns True if a given string is valid parentheses expression.

    Args:
        expression: str, input string for validation.
    Returns:
        bool, whether a given string is valid parentheses expression.
    """
    stack = Stack()
    parentheses_simbols = {')': '(', ']': '[', '}': '{'}
    open_parentheses = set(parentheses_simbols.values())

    for char in expression:
        if char in open_parentheses:
            stack.push(char)
        elif char in parentheses_simbols:
            if stack.empty() or stack.peak() != parentheses_simbols[char]:
                return False
            stack.pop()
        else:
            continue

    return stack.empty()
