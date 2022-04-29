import pytest

from random import randint

from binary_search import binary_search


def generate_binary_search_data():
    data = []
    for length in range(100, 10000, 100):
        arr = [i for i in range(0, length, 17)]
        idx = randint(0, len(arr) - 1)
        data.append((arr, arr[idx], idx))
    return data


@pytest.mark.parametrize("arr, value, result", generate_binary_search_data())
def test_binary_search(arr, value, result):
    assert binary_search(arr, value) == result
