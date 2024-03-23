"""Template for programming assignment: Reverse Polish notation."""
from typing import List


def evaluate_rpn_tokens(rpn_tokens: List[str]) -> int:
    """Returns the evaluation result of a given list of RPN tokens."""
    operand_stack = []
    for token in rpn_tokens:
        if token.isdigit():
            operand_stack.append(int(token))
        else:
            operand_two = operand_stack.pop()
            operand_one = operand_stack.pop()
            if token == '+':
                operand_stack.append(operand_one + operand_two)
            elif token == '-':
                operand_stack.append(operand_one - operand_two)
            elif token == '*':
                operand_stack.append(operand_one * operand_two)
            elif token == '/':
                operand_stack.append(int(operand_one / operand_two))
    return operand_stack[0]
