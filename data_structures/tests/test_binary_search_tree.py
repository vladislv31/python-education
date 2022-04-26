import pytest

from binary_search_tree import BinarySearchTree


@pytest.fixture(name="bst")
def fixture_bst():
    """Returns bst with no elements."""
    return BinarySearchTree()

@pytest.fixture(name="filled_bst")
def fixture_filled_bxt():
    """Returns bst with some elements."""
    return BinarySearchTree([5, 20, 15, 3, 4, 2, 35, 20, 13, 16, 36, 25, 38, 37])


@pytest.mark.parametrize("to_insert, expected", [
    ([5, 10, 4, 3, 2, 1, 25], [5, 10, 25, 4, 3, 2, 1]),
    ([1, 2, 3, 0, -5, -10, -3, 5, 4, 6], [1, 2, 3, 5, 6, 4, 0, -5, -3, -10]),
    ([100, 95, 100, 5, -5, 0, 2, 120, 111, 125, 123, 126], [100, 120, 125, 126, 123, 111, 95, 5, -5, 0, 2]),
])
def test_insert(bst, to_insert, expected):
    for insert in to_insert:
        bst.insert(insert)
    assert list(bst) == expected

@pytest.mark.parametrize("to_lookup", [
    5, 35, 20, 3, 4
])
def test_lookup(filled_bst, to_lookup):
    node = filled_bst.lookup(to_lookup)
    assert node.val == to_lookup

@pytest.mark.parametrize("to_lookup", [
    100, 120, -5, -99, 0
])
def test_lookup_none(filled_bst, to_lookup):
    node = filled_bst.lookup(to_lookup)
    assert node == None

@pytest.mark.parametrize("to_delete, expected", [
    (15, [5, 20, 35, 36, 38, 37, 25, 13, 16, 3, 4, 2]),
    (5, [4, 20, 35, 36, 38, 37, 25, 15, 16, 13, 3, 2]),
    (20, [5, 16, 35, 36, 38, 37, 25, 15, 13, 3, 4, 2]),
    (25, [5, 20, 35, 36, 38, 37, 15, 16, 13, 3, 4, 2]),
    (36, [5, 20, 35, 38, 37, 25, 15, 16, 13, 3, 4, 2]),
    (4, [5, 20, 35, 36, 38, 37, 25, 15, 16, 13, 3, 2]),
    (38, [5, 20, 35, 36, 37, 25, 15, 16, 13, 3, 4, 2]),
])
def test_delete(filled_bst, to_delete, expected):
    filled_bst.delete(to_delete)
    assert list(filled_bst) == expected

@pytest.mark.parametrize("to_delete", [
    -100, 0, 100, 95, 26, 17
])
def test_delete_value_error(filled_bst, to_delete):
    with pytest.raises(ValueError):
        filled_bst.delete(to_delete)