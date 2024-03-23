"""Templates for programming assignments: stack API."""
from typing import Any, Optional


class Stack:
    """Default interface for Stack data structure."""

    def __init__(self):
        self._stack = []
        self.min_stack = []        

    def empty(self) -> bool:
        """Returns True if the stack is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        return len(self._stack) == 0

    def size(self) -> int:
        """Returns the number of elements within the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        return len(self._stack)

    def push(self, element: Any):
        """Adds a given element to the top of the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        self._stack.append(element)
        if len(self.min_stack) == 0:
            self.min_stack.append(element)
        else:
            if element < self.min_stack[-1]:
                self.min_stack.append(element)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> Any:
        """Returns the top element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        if len(self._stack) == 0:
            raise ValueError
        self.min_stack.pop()
        return self._stack.pop()

    def peak(self) -> Any:
        """Returns the top element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        if len(self._stack) == 0:
            raise ValueError
        return self._stack[-1]


class StackWithMinimum(Stack):
    """Extended Stack class that supports `get_minimum` operation.

    Assume that elements in Stack are numerical (so that `get_minimum` operation is eligible).
    """

    def get_minimum(self) -> Optional[int]:
        """Returns the minimum element in the stack.

        NOTE: if the stack is empty - return None.
        NOTE: O(1) complexity is expected for this operation.
        """
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]
