import pytest

import copy
from random import randint

from stack import Stack


def generate_push_data():
    data = []
    for i in range(50):
        items = [item for item in range(0, 100, 7)]
        to_push = randint(0, 100)
        data.append((items, to_push))
    return data

def generate_pop_peek_data():
    data = []
    for i in range(50):
        items = [item for item in range(0, 100, 7)]
        data.append(items)
    return data


def test_init():
    stack = Stack()
    assert list(stack) == []

def test_init_items():
    stack = Stack([1, 2, 3])
    assert list(stack) == [3, 2, 1]

@pytest.mark.parametrize("items, to_push", generate_push_data())
def test_push(items, to_push):
    stack = Stack(items)
    expected = [to_push] + list(reversed(items))
    stack.push(to_push)
    assert list(stack) == expected

@pytest.mark.parametrize("items", generate_pop_peek_data())
def test_pop(items):
    stack = Stack(items)
    expected = list(reversed(items))[1:]
    stack.pop()
    assert list(stack) == expected

@pytest.mark.parametrize("items", generate_pop_peek_data())
def test_pop_result(items):
    stack = Stack(items)
    result = items[-1]
    assert stack.pop() == result

@pytest.mark.parametrize("items", generate_pop_peek_data())
def test_peek(items):
    stack = Stack(items)
    stack_list = list(copy.deepcopy(stack))
    stack.peek()
    assert list(stack) == stack_list

@pytest.mark.parametrize("items, result", [
    ([], None),
    ([1, 2, 3], 3),
    ([5, 4, 6], 6),
])
def test_peek_result(items, result):
    stack = Stack(items)
    assert stack.peek() == result