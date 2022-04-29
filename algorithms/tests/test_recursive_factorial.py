import pytest

from recursive_factorial import fact


@pytest.mark.parametrize("to_fact, result", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
])
def test_recursive_factorial(to_fact, result):
    assert fact(to_fact) == result
