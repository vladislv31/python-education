import pytest

from random import randint, choice

from hash_table import HashTable


def generate_insert_data():
    data = []
    for i in range(100):
        items = []
        for key in range(0, 100, 3):
            value = randint(0, 100)
            value = randint(0, 100)
            items.append((key, value))
        items = set(items)
        to_insert = (randint(100, 150), randint(0, 100))
        data.append((items, to_insert))
    return data

def generate_lookup_data():
    data = []
    for i in range(100):
        items = []
        for key in range(0, 100, 3):
            value = randint(0, 100)
            value = randint(0, 100)
            items.append((key, value))
        to_lookup = choice(items)
        to_lookup, to_lookup_res = to_lookup[0], to_lookup[1]
        items = set(items)
        data.append((items, to_lookup, to_lookup_res))
    return data

def generate_delete_data():
    data = []
    for i in range(100):
        items = []
        for key in range(0, 100, 3):
            value = randint(0, 100)
            value = randint(0, 100)
            items.append((key, value))
        to_delete_idx = randint(0, len(items) - 1)
        to_delete = items[to_delete_idx][0]
        expected = items[:to_delete_idx] + items[to_delete_idx + 1:]
        items = set(items)
        expected = set(expected)
        data.append((items, to_delete, expected))
    return data


@pytest.fixture(name="filled_hash_table")
def fixture_filled_hash_table():
    """Returns hashtable with 5 elements"""
    hash_table = HashTable(50)
    hash_table.insert("key", "value")
    hash_table.insert(5, 10)
    hash_table.insert(-5, 20)
    hash_table.insert(0, "zero")
    hash_table.insert(None, "some")
    return hash_table


@pytest.mark.parametrize("items, to_insert", generate_insert_data())
def test_insert(items, to_insert):
    table = HashTable()
    for item in items:
        table.insert(item[0], item[1])
    table.insert(to_insert[0], to_insert[1])
    expected = items.union({to_insert})
    assert set(table) == expected

@pytest.mark.parametrize("items, to_lookup, to_lookup_res", generate_lookup_data())
def test_lookup(items, to_lookup, to_lookup_res):
    table = HashTable()
    for item in items:
        table.insert(item[0], item[1])
    assert table.lookup(to_lookup) == to_lookup_res

@pytest.mark.parametrize("key", ["undefined", 100, -100])
def test_lookup_key_error(filled_hash_table, key):
    with pytest.raises(KeyError):
        filled_hash_table.lookup(key)

@pytest.mark.parametrize("items, to_delete, expected", generate_delete_data())
def test_delete(items, to_delete, expected):
    table = HashTable()
    for item in items:
        table.insert(item[0], item[1])
    table.delete(to_delete)
    assert set(table) == expected

@pytest.mark.parametrize("key", [-100, "undefined", 55])
def test_delete_key_error(filled_hash_table, key):
    with pytest.raises(KeyError):
        filled_hash_table.delete(key)
