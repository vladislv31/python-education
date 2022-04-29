"""Module with implemented base classes"""

from abc import ABC


class BaseList(ABC):
    """Base List"""

    def __init__(self):
        self._head = None

    def _append(self, val):
        """Adds val into end of the base list.

        Args:
            val: object to add.
        """
        node = Node(val)

        if self._head is None:
            self._head = node
        else:
            current_node = self._head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = node

    def _prepend(self, val):
        """Adds val into start of the base list.

        Args:
            val: object to add.
        """
        node = Node(val, self._head)
        self._head = node

    def _lookup(self, val, compare_field=None):
        """Returns idx of first searched node with such value.

        Args:
            val: value to search.

        Returns:
            int: idx of node if node with such val was found.
            None: if node was not found.
        """
        current_node = self._head

        idx = 0
        while current_node is not None:
            if compare_field:
                if getattr(current_node.val, compare_field) == getattr(val, compare_field):
                    return idx
            else:
                if current_node.val == val:
                    return idx
            idx += 1
            current_node = current_node.next

        return None

    def _get_node_by_idx(self, idx):
        """Returns node by idx

        Args:
            idx (int): idx to search.

        Returns:
            Node: if node was found.
            None: if node was not found.
        """
        current_node = self._head

        current_idx = 0
        while current_node is not None:
            if current_idx == idx:
                return current_node
            current_idx += 1
            current_node = current_node.next

        return None

    def _insert(self, idx, val):
        """Inserts val to specific place in base list.

        Args:
            idx (int): idx of new node.
            val: object value of new node.
        """
        if idx == 0:
            self._prepend(val)
        else:
            current_node = self._get_node_by_idx(idx - 1)
            if current_node is None:
                self._append(val)
            else:
                current_node.next = Node(val, current_node.next)

    def _delete(self, idx):
        """Deletes node with such idx.

        Args:
            idx (int): idx of node to delete.

        Raises:
            IndexError: when node with such idx not found.
        """
        if idx == 0 and self._head:
            self._head = self._head.next
        else:
            node = self._get_node_by_idx(idx - 1)
            if node is None or node.next is None:
                raise IndexError("No element found with such index.")
            node.next = None if not node.next else node.next.next

    def _length(self):
        length = 0
        node = self._head
        while node is not None:
            length += 1
            node = node.next
        return length


class Node:
    """Node Class.

    Args:
        val: value of node.
        next_ (Node, optional): link to next node.
    """

    def __init__(self, val, next_=None):
        self._val = val
        self._next = next_

    @property
    def val(self):
        """Returns node value.

        Returns:
            Object: value object.
        """
        return self._val

    @property
    def next(self):
        """Returns next node link.

        Returns:
            Node: next node link.
            None: if node has not next node link.
        """
        return self._next

    @next.setter
    def next(self, new_next):
        """Changes next node link.

        Args:
            new_next (Node|None): new next node link.
        """
        self._next = new_next
