# Stack (python)

Set of programming assignments that are designed to test knowledge of stack data structure.

### Default interface for Stack data structure

The following snippet contains the default interface that could be used for implements Stack data structure. Of course the interface could be expanded with additional method if needed.

```python
class Stack:
    """Default interface for Stack data structure."""

    def __init__(self):
        pass

    def empty(self) -> bool:
        """Returns True if the stack is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def size(self) -> int:
        """Returns the number of elements within the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def push(self, element: Any):
        """Adds a given element to the top of the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def pop(self) -> Any:
        """Returns the top element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        pass

    def peak(self) -> Any:
        """Returns the top element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        pass
```

You may find the interface above here: `tasks/stack.py`.

## Problem 1: Implement stack using the default interface

Your first programming assignment is to implement the provided default interface for Stack above.
Tests will check your implementation in different scenarios, for simplicity you may assume that only numeric elements will be used for testing.


Please use a template for the implementation (`tasks/stack.py`).

## Problem 2: Check whether a given parentheses expression is valid

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1:**

Input: `s='()'`

Expected result: True.

**Example 2:**

Input: `s='()[]{}'`

Expected result: True.

**Example 3:**

Input: `s='([})'`

Expected result: True.


Please use a template for the implementation (`tasks/parentheses.py`).

## Problem 3: Stack with minimum operation

Let's extend the default interface of Stack data structure and add a support of `get_minimum` method:

```python
class StackWithMinimum(Stack):  # Here we inherit from the default interface, make sure it is implemented already.
    """Extended Stack class that supports minimum operation.

    Assume that elements of stack are numerical (so that minimum operation is eligible).
    """

    def get_minimum(self) -> Optional[int]:
        """Returns the minimum element in the stack.

        NOTE: if the stack is empty - return None.
        NOTE: O(1) complexity is expected for this operation.
        """
        pass
```

**Example:**


```python
stack = StackWithMinimum()
stack.push(3)  # 3
stack.push(2)  # 3, 2
stack.push(4)  # 3, 2, 4

assert stack.get_minimum() == 2

stack.push(5)  # 3, 2, 4, 5
stack.push(1)  # 3, 2, 4, 5, 1

assert stack.get_minimum() == 1

stack.pop()  # 3, 2, 4, 5
stack.pop()  # 3, 2, 4

assert stack.get_minimum() == 2
```

Please use a template for the implementation (`tasks/stack.py`).


## Problem 4: Reverse Polish notation parsing

Your task is to evaluate the value of an arithmetic expression in [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


**Example 1:**

Input: `tokens = ["3","2","+","10","*"]`

Expected result: 50.

Explanation: `(3 + 2) * 10 = 50`

**Example 2:**

Input: `tokens = ["10", "4", "-", "2", "*", "4", "/"]`

Expected result: 2.

Explanation: `((10 - 4) * 2) / 5 = 2`

Please use a template for the implementation (`tasks/rpn.py`).
