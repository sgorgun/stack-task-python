"""Templates for programming assignments: stack API."""
from typing import Any, Optional

class LinkedListNode:
    """Dataclass that represents linked list elements."""

    def __init__(
        self,
        value: int = 0,
        next_element: Optional['LinkedListNode'] = None
    ):
        self.value = value
        self.next_element = next_element

class Stack:
    """Default interface for Stack data structure."""

    def __init__(self):
        self.head = None
        self.counter = 0
        self.min_stack = None

    def empty(self) -> bool:
        """Returns True if the stack is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        return self.head is None

    def size(self) -> int:
        """Returns the number of elements within the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        return self.counter

    def push(self, element: Any):
        """Adds a given element to the top of the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        new_node = LinkedListNode(element, self.head)
        self.head = new_node
        self.counter += 1
        
        if self.min_stack is None or element <= self.min_stack.value:
            self.min_stack = LinkedListNode(element, self.min_stack)

    def pop(self) -> Any:
        """Returns the top element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.empty():
            raise ValueError("Stack is empty")
        result = self.head.value
        self.head = self.head.next_element
        self.counter -= 1
        
        if result == self.min_stack.value:
            self.min_stack = self.min_stack.next_element
        
        return result

    def peak(self) -> Any:
        """Returns the top element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.empty():
            raise ValueError("Stack is empty")
        return self.head.value

class StackWithMinimum(Stack):
    """Extended Stack class that supports `get_minimum` operation.

    Assume that elements in Stack are numerical (so that `get_minimum` operation is eligible).
    """

    def get_minimum(self) -> Optional[int]:
        """Returns the minimum element in the stack.

        NOTE: if the stack is empty - return None.
        NOTE: O(1) complexity is expected for this operation.
        """
        if self.empty():
            return None
        return self.min_stack.value