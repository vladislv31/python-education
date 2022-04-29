import pytest

from random import randint

from linked_list import LinkedList


@pytest.fixture(name="filled_linked_list")
def fixture_filled_linked_list():
    """Returns Linked List with 7 elements"""
    return LinkedList([1, 2, 3, 3, 4, 5, 5])


def generate_add_data():
    data = []
    for i in range(100):
        items = [item for item in range(0, 100, 17)]
        to_insert = randint(0, 100)
        data.append((items, to_insert))
    return data

def generate_insert_data():
    data = []
    for i in range(100):
        items = [item for item in range(0, 1000, 17)]
        to_insert_idx = randint(0, len(items) - 1)
        to_insert_value = randint(0, 1000)
        data.append((items, to_insert_idx, to_insert_value))
    return data

def generate_lookup_data():
    data = []
    for i in range(10):
        items = [item for item in range(0, 100, 1)]
        to_lookup_idx = randint(0, len(items) - 1)
        to_lookup_val = items[to_lookup_idx]
        data.append((items, to_lookup_idx, to_lookup_val))
    return data

def generate_delete_data():
    data = []
    for i in range(100):
        items = [item for item in range(0, 1000, 17)]
        to_delete_idx = randint(0, len(items) - 1)
        data.append((items, to_delete_idx))
    return data


def test_init():
    linked_list = LinkedList()
    assert list(linked_list) == []

def test_init_items():
    linked_list = LinkedList([1, 2, 3])
    assert list(linked_list) == [1, 2, 3]

@pytest.mark.parametrize("items, to_insert", generate_add_data())
def test_append(items, to_insert):
    linked_list = LinkedList(items)
    expected = items[:] + [to_insert]
    linked_list.append(to_insert)
    assert list(linked_list) == expected

@pytest.mark.parametrize("items, to_insert", generate_add_data())
def test_prepend(items, to_insert):
    linked_list = LinkedList(items)
    expected = [to_insert] + items[:]
    linked_list.prepend(to_insert)
    assert list(linked_list) == expected

@pytest.mark.parametrize("items, to_lookup, to_lookup_val", generate_lookup_data())
def test_lookup(items, to_lookup, to_lookup_val):
    linked_list = LinkedList(items)
    assert linked_list.lookup(to_lookup) == to_lookup_val

@pytest.mark.parametrize("items, insert_idx, insert_val", generate_insert_data())
def test_insert(items, insert_idx, insert_val):
    linked_list = LinkedList(items)
    expected = items[:insert_idx] + [insert_val] + items[insert_idx:]
    linked_list.insert(insert_idx, insert_val)
    assert list(linked_list) == expected

@pytest.mark.parametrize("items, to_delete", generate_delete_data())
def test_delete(items, to_delete):
    linked_list = LinkedList(items)
    expected = items[:to_delete] + items[to_delete + 1:]
    linked_list.delete(to_delete)
    assert list(linked_list) == expected

@pytest.mark.parametrize("delete", [7, 8, -1, 9, 10])
def test_delete_index_error(filled_linked_list, delete):
    with pytest.raises(IndexError):
        filled_linked_list.delete(delete)
