"""Module with implemented class LinkedList"""

from base_list import BaseList


class LinkedList(BaseList):
    """Linked List

    Args:
        items (list, optional): initial linked list items.
    """

    def __init__(self, items=None):
        super().__init__()
        if items is not None:
            for item in items:
                self.append(item)

    def append(self, val):
        """Adds val into end of the linked list."""
        self._append(val)

    def prepend(self, val):
        """Adds val into start of the linked list.

        Args:
            val: object to add.
        """
        self._prepend(val)

    def lookup(self, val, compare_filed=None):
        """Returns idx of first searched node with such value.

        Args:
            val: value to search.
            compare_filed (str, optional): field name for comparing.

        Returns:
            int: idx of node if node with such val was found.
            None: if node was not found.
        """
        return self._lookup(val, compare_filed)

    def insert(self, idx, val):
        """Inserts val to specific place in linked list.

        Args:
            idx (int): idx of new node.
            val: object value of new node.
        """
        self._insert(idx, val)

    def delete(self, idx):
        """Deletes node with such idx.

        Args:
            idx (int): idx of node to delete.

        Raises:
            IndexError: when node with such idx not found.
        """
        self._delete(idx)

    def length(self):
        """Returns length of linked list"""
        return self._length()

    def __iter__(self):
        return LinkedListIterator(self._head)


class LinkedListIterator:
    """Linked list iterator.

    Args:
        node (Node): head of data structure.
    """

    def __init__(self, node):
        self._node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self._node is None:
            raise StopIteration
        val = self._node.val
        self._node = self._node.next
        return val
