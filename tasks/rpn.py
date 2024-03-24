"""Template for programming assignment: Reverse Polish notation."""
from typing import List
from tasks.stack import Stack, LinkedListNode


def evaluate_rpn_tokens(rpn_tokens: List[str]) -> int:
    """Returns the evaluation result of a given list of RPN tokens."""
    operand_stack = Stack()
    for token in rpn_tokens:
        if token.lstrip('-').isdigit():  # This will handle negative numbers
            operand_stack.push(int(token))
        else:
            if operand_stack.size() < 2:
                raise ValueError("Invalid RPN expression: not enough operands for operation")
            operand_two = operand_stack.pop()
            operand_one = operand_stack.pop()
            if token == '+':
                operand_stack.push(operand_one + operand_two)
            elif token == '-':
                operand_stack.push(operand_one - operand_two)
            elif token == '*':
                operand_stack.push(operand_one * operand_two)
            elif token == '/':
                operand_stack.push(int(operand_one / operand_two))
    if operand_stack.size() != 1:
        raise ValueError("Invalid RPN expression: too many operands")
    return operand_stack.pop()
