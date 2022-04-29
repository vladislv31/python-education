"""Module implements quick sort."""


def partition(arr, start, end):
    """Diving subarray by pivot.

    Args:
        arr: list to divide.
        start: start index for subarray.
        end: end index for subarray.

    Returns:
        int: index of wall.
    """
    pivot = arr[end]
    wall = start - 1

    for idx in range(start, end):
        if arr[idx] <= pivot:
            wall += 1
            arr[idx], arr[wall] = arr[wall], arr[idx]

    wall += 1
    arr[wall], arr[end] = arr[end], arr[wall]

    return wall


def quick_sort(arr):
    """Sorting list with quick sort algorithm.

    Args:
        arr: list to sort.
    """
    length = len(arr)
    stack = [0] * length
    top = -1

    top += 1
    stack[top] = 0
    top += 1
    stack[top] = length - 1

    while top >= 0:
        end = stack[top]
        top -= 1
        start = stack[top]
        top -= 1

        pivot = partition(arr, start, end)
        if pivot - 1 > start:
            top += 1
            stack[top] = start
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < end:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = end
