import pytest

from datetime import datetime

import shop
from shop import even_odd, sum_all, time_of_day


@pytest.mark.parametrize("number, result", [
    (0, "even"),
    (1, "odd"),
    (2, "even"),
    (3, "odd"),
    (4, "even"),
    (5, "odd"),
    (6, "even"),
    (7, "odd"),
    (8, "even"),
    (9, "odd"),
])
def test_even_odd(number, result):
    assert even_odd(number) == result

@pytest.mark.parametrize("numbers, sum", [
    ([1, 1.5, 5], 7.5),
    ([2, 3, 5], 10),
    ([1, 2, 3, 4], 10),
    ([2.5, 0, -1], 1.5),
])
def test_sum_all(numbers, sum):
    assert sum_all(*numbers) == sum

@pytest.mark.parametrize("hour, result", [
    (0, "night"),
    (1, "night"),
    (2, "night"),
    (3, "night"),
    (4, "night"),
    (5, "night"),
    (6, "morning"),
    (7, "morning"),
    (8, "morning"),
    (9, "morning"),
    (10, "morning"),
    (11, "morning"),
    (12, "afternoon"),
    (13, "afternoon"),
    (14, "afternoon"),
    (15, "afternoon"),
    (16, "afternoon"),
    (17, "afternoon"),
    (18, "night"),
    (19, "night"),
    (21, "night"),
    (22, "night"),
    (23, "night"),
])
def test_time_of_day(monkeypatch, hour, result):
    class MockResponse:

        @classmethod
        def now(self):
            return datetime(2022, 1, 1, hour, 0, 0, 0)

    monkeypatch.setattr(shop, 'datetime', MockResponse)
    assert time_of_day() == result