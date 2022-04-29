import pytest

from graph import Graph


@pytest.fixture(name="graph")
def fixture_graph():
    """Returns graph"""
    return Graph()


def test_insert(graph):
    graph.insert("A")
    a = graph.lookup("A")

    graph.insert("B", [a])
    b = graph.lookup("B")

    graph.insert("C", [a])
    c = graph.lookup("C")

    graph.insert("E", [a, b])
    assert set(graph) == {("A", frozenset(["B", "E", "C"])), ("B", frozenset(["A", "E"])), ("C", frozenset(["A"])), ("E", frozenset(["A", "B"]))}

def test_insert_value_error(graph):
    graph.insert("A")
    a = graph.lookup("A")
    graph.delete(a)

    with pytest.raises(ValueError):
        graph.insert("B", [a])

def test_lookup(graph):
    graph.insert("A")
    a = graph.lookup("A")

    assert graph.lookup("A") == a

def test_lookup_none(graph):
    graph.insert("A")
    a = graph.lookup("A")
    graph.delete(a)

    assert graph.lookup("A") == None

def test_delete(graph):
    graph.insert("A")
    a = graph.lookup("A")

    graph.insert("B", [a])
    b = graph.lookup("B")

    graph.insert("C", [a])

    graph.insert("E", [a, b])
    graph.delete(a)
    assert set(graph) == {("B", frozenset(["E"])), ("C", frozenset()), ("E", frozenset(["B"]))}
