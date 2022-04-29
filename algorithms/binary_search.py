"""Module implements binary search"""


def binary_search(arr, val):
    """Binary search function.

    Args:
        arr(list): list where val need to be searched.
        val: value to search.
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        idx = (start + end) // 2
        if val == arr[idx]:
            return idx
        if val < arr[idx]:
            end = idx - 1
        else:
            start = idx + 1


if __name__ == '__main__':
    print(binary_search([0, 17, 34, 51, 68, 85], 17))
