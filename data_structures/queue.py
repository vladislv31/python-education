"""Module implements class Queue"""

from base_list import BaseList


class Queue(BaseList):
    """Class Queue.

    Args:
        items (list, optional): initial items for queue.
    """

    def __init__(self, items=None):
        super().__init__()
        if items is not None:
            for item in items:
                self.enqueue(item)

    def enqueue(self, val):
        """Adds node to start of the queue.

        Args:
            val: value of new node.
        """
        self._append(val)

    def dequeue(self):
        """Removes node from the end of the queue.

        Returns:
            object: value of deleted node.
            None: if queue is empty.
        """
        if self._head is None:
            return None
        val = self._head.val
        self._head = self._head.next
        return val

    def peek(self):
        """Returns val from start of the queue.

        Returns:
            object: if queue is not empty.
            None: if queue is empty.
        """
        if self._head is None:
            return None
        return self._head.val

    def __iter__(self):
        return QueueIterator(self)


class QueueIterator:
    """Iterator for Queue.

    Args:
        queue(Queue): queue
    """

    def __init__(self, queue):
        self._queue = queue

    def __iter__(self):
        return self

    def __next__(self):
        val = self._queue.dequeue()
        if val is None:
            raise StopIteration
        return val
