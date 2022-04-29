"""Module implements Graph class"""

from linked_list import LinkedList


class Graph:
    """Graph class"""

    def __init__(self):
        self._nodes = LinkedList()

    def insert(self, val, neighbors=None):
        """Inserts node.

        Args:
            val(object): value of node.
            neighbors(Node[], optional): list of neighbors.

        Raises:
            ValueError: if found unknown neighbor.
        """
        if neighbors is None:
            neighbors = []
        if not all(neighbor in self._nodes for neighbor in neighbors):
            raise ValueError("Some neighbor was not found.")

        node = Node(val)
        for neighbor in neighbors:
            node.neighbors.append(neighbor)
            neighbor.neighbors.append(node)

        self._nodes.append(node)

    def lookup(self, val):
        """Lookups node by val.

        Args:
            val: value of node.

        Returns:
            Node: if found.
            None: if node not found.
        """
        for node in self._nodes:
            if node.val == val:
                return node

    def delete(self, node):
        """Deletes node by link.

        Args:
            node(Node): link to node to delete.
        """
        for neighbor in node.neighbors:
            idx = neighbor.neighbors.lookup(node)
            neighbor.neighbors.delete(idx)
        idx = self._nodes.lookup(node)
        self._nodes.delete(idx)

    def __iter__(self):
        return GraphIterator(self._nodes)


class GraphIterator:
    """Graph Iterator.

    Args:
        nodes (LinkedList): graph nodes.
    """

    def __init__(self, nodes):
        self._nodes_iter = iter(nodes)

    def __iter__(self):
        return self

    def __next__(self):
        node = next(self._nodes_iter)
        return node.val, frozenset([n.val for n in node.neighbors])


class Node:
    """Node class for Graph.

    Args:
        val: value of node.
    """

    def __init__(self, val):
        self.val = val
        self.neighbors = LinkedList()

    def __repr__(self):
        return f"Node(val={self.val}, neighbors={[neighbor.val for neighbor in self.neighbors]})"
