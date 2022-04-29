"""Module implements class Stack"""

from base_list import BaseList


class Stack(BaseList):
    """Stack Class.

    Args:
        items (list, optional): initial stack items.
    """

    def __init__(self, items=None):
        super().__init__()
        if items is not None:
            for item in items:
                self.push(item)

    def push(self, val):
        """Adds val to stack.

        Args:
            val: value of new node.
        """
        self._prepend(val)

    def pop(self):
        """Removes node from stack.

        Returns:
            Object: value of removed node.
            None: if stack is empty.
        """
        if self._head is None:
            return None
        val = self._head.val
        self._head = self._head.next
        return val

    def peek(self):
        """Returns val from next to pop node of the stack.

        Returns:
            object: if queue is not empty.
            None: if queue is empty.
        """
        if self._head is None:
            return None
        return self._head.val

    def __iter__(self):
        return StackIterator(self)


class StackIterator:
    """Iterator for Stack.

    Args:
        stack(Stack): stack
    """

    def __init__(self, stack):
        self._stack = stack

    def __iter__(self):
        return self

    def __next__(self):
        val = self._stack.pop()
        if val is None:
            raise StopIteration
        return val
