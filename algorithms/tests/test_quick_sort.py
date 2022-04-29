import pytest

from random import shuffle

from quick_sort import quick_sort


def generate_quick_sort_data():
    data = []
    for length in range(100, 10000, 100):
        arr = [i for i in range(0, length, 17)]
        shuffle(arr)
        data.append(arr)
    return data


@pytest.mark.parametrize("arr", generate_quick_sort_data())
def test_quick_sort(arr):
    quick_sort(arr)
    assert arr == sorted(arr)
