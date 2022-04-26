import pytest

import copy
from random import randint

from queue import Queue


def generate_enqueue_data():
    data = []
    for i in range(50):
        items = [item for item in range(0, 100, 7)]
        to_enq = randint(0, 100)
        data.append((items, to_enq))
    return data

def generate_dequeue_peek_data():
    data = []
    for i in range(50):
        items = [item for item in range(0, 100, 7)]
        data.append(items)
    return data


def test_init():
    queue = Queue()
    assert list(queue) == []

def test_init_items():
    queue = Queue([1, 2, 3])
    assert list(queue) == [1, 2, 3]

@pytest.mark.parametrize("items, enqueue", generate_enqueue_data())
def test_enqueue(items, enqueue):
    queue = Queue(items)
    expected = items + [enqueue]
    queue.enqueue(enqueue)
    assert list(queue) == expected

@pytest.mark.parametrize("items", generate_dequeue_peek_data())
def test_dequeue(items):
    queue = Queue(items)
    expected = items[1:]
    queue.dequeue()
    assert list(queue) == expected

@pytest.mark.parametrize("items", generate_dequeue_peek_data())
def test_dequeue_result(items):
    queue = Queue(items)
    result = items[0]
    assert queue.dequeue() == result

@pytest.mark.parametrize("items", generate_dequeue_peek_data())
def test_peek(items):
    queue = Queue(items)
    queue_list = list(copy.deepcopy(queue))
    queue.peek()
    assert queue_list == list(queue)

@pytest.mark.parametrize("items", generate_dequeue_peek_data())
def test_peek_result(items):
    queue = Queue(items)
    result = items[0]
    assert queue.peek() == result