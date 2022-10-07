"""Templates for programming assignments: stack API."""
from typing import Any, Optional


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


class StackWithMinimum(Stack):
    """Extended Stack class that supports `get_minimum` operation.

    Assume that elements in Stack are numerical (so that `get_minimum` operation is eligible).
    """

    def get_minimum(self) -> Optional[int]:
        """Returns the minimum element in the stack.

        NOTE: if the stack is empty - return None.
        NOTE: O(1) complexity is expected for this operation.
        """
        pass
