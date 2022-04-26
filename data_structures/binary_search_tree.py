"""Module implements Binary Search Tree Class"""

from stack import Stack


class BinarySearchTree:
    """BinarySearchTree Class.

    Args:
        items(list, optional): list of initial items.
    """

    def __init__(self, items=None):
        self._root = None
        if items is not None:
            for item in items:
                self.insert(item)

    def insert(self, val):
        """Inserts value to tree.

        Args:
            val: value of new node.
        """
        if self._root is None:
            self._root = Node(val)
        else:
            node = self._root
            while True:
                if val < node.val:
                    if node.left is not None:
                        node = node.left
                    else:
                        node.left = Node(val, parent=node)
                        break
                elif val == node.val:
                    break
                else:
                    if node.right is not None:
                        node = node.right
                    else:
                        node.right = Node(val, parent=node)
                        break

    def lookup(self, val):
        """Lookups for node by val.

        Args:
            val: value of node.

        Returns:
            Node: if found.
            None: if node not found.
        """
        node = self._root
        while node is not None:
            if val == node.val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, val):
        """Deletes node by val.

        Args:
            val: value of node to delete.

        Raises:
            ValueError: if node not found.
        """
        node = self.lookup(val)
        if node is None:
            raise ValueError("Node with such value not found.")
        else:
            if node.left is None and node.right is None:
                if node.parent is None:
                    self._root = None
                else:
                    if node.val > node.parent.val:
                        node.parent.right = None
                    else:
                        node.parent.left = None
            elif node.left is not None and node.right is not None:
                min_node = node.left
                while min_node.right is not None:
                    min_node = min_node.right
                if node.parent is None:
                    self._root.val = min_node.val
                else:
                    node.val = min_node.val
                if min_node.val > min_node.parent.val:
                    min_node.parent.right = None
                else:
                    min_node.parent.left = None
            elif node.left is not None:
                if node.parent is None:
                    self._root = node.left
                else:
                    if node.val > node.parent.val:
                        node.parent.right = node.left
                    else:
                        node.parent.left = node.left
            elif node.right is not None:
                if node.parent is None:
                    self._root = node.right
                else:
                    if node.val > node.parent.val:
                        node.parent.right = node.right
                    else:
                        node.parent.left = node.right

    def __iter__(self):
        stack = Stack()
        stack.push(self._root)

        while stack.peek() is not None:
            node = stack.pop()
            yield node.val
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)


class Node:
    """Node for Binary Search Tree.

    Args:
        val: value of node.
        left (Node, optional): link to left child.
        right (Node, optional): link to right child.
        parent (Node, optional): link to parent.
    """

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"
