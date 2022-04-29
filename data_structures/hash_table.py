"""Module implements HashTable Class"""

from itertools import chain

from linked_list import LinkedList


class HashTable:
    """HastTable class.

    Args:
        length (int, optional): length of table.
    """

    def __init__(self, length=100):
        self._length = length
        self._table = [None for _ in range(length)]

    def _hash(self, key):
        """Returns hash for key.

        Args:
            key: object with implemented str method.
        """
        idx = 0
        for char in str(key):
            idx += ord(char)
        return idx % self._length

    def insert(self, key, value):
        """Inserts value by key.

        Args:
            key: object with implemented str method.
            value: object to add.
        """
        idx = self._hash(key)
        item = Item(key, value)
        if self._table[idx] is None:
            self._table[idx] = item
        elif isinstance(self._table[idx], LinkedList):
            item_idx = self._table[idx].lookup(item, 'key')
            if item_idx is None:
                self._table[idx].append(item)
            else:
                self._table[idx].delete(item_idx)
                self._table[idx].insert(item_idx, item)
        else:
            if self._table[idx].key == key:
                self._table[idx].value = value
            else:
                self._table[idx] = LinkedList([self._table[idx], item])


    def lookup(self, key):
        """Looks for key in a table and returns its value if found.

        Args:
            key: object with implemented str method.

        Returns:
            value: object that refers to key.

        Raises:
            KeyError: if no item found.
        """
        idx = self._hash(key)
        if isinstance(self._table[idx], LinkedList):
            for item in self._table[idx]:
                if item.key == key:
                    return item.value
        elif self._table[idx] is not None:
            if self._table[idx].key == key:
                return self._table[idx].value
        raise KeyError("No item with such key.")

    def delete(self, key):
        """Delets item from table by key.

        Returns:
            value: object that refers to key.

        Raises:
            KeyError: if no item found.
        """
        idx = self._hash(key)
        if isinstance(self._table[idx], LinkedList):
            for item_idx, item in enumerate(self._table[idx]):
                if item.key == key:
                    self._table[idx].delete(item_idx)
                    if self._table[idx].length() == 1:
                        self._table[idx] = list(self._table[idx])[0]
                    return
        elif self._table[idx] is not None:
            if self._table[idx].key == key:
                self._table[idx] = None
                return
        raise KeyError("No item with such key.")

    def __iter__(self):
        return HashTableIterator(self._table)


class HashTableIterator:
    """HastTable Iterator"""

    def __init__(self, table):
        self._items = chain(*(filter(lambda i: i is not None, table)))

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._items)
        return (item.key, item.value)


class Item:
    """HashTable Item.

    Args:
        key: object.
        value: object.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __iter__(self):
        yield self
