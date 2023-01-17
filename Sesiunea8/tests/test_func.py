import unittest
from parameterized import parameterized
from Sesiunea8.app.func import is_div_3_5, NotIntegerNumberException, only_ints
import pytest


class TestFunc(unittest.TestCase):
    def test_is_div_3_5_35(self):
        self.assertEqual(is_div_3_5(45), 35)

    def test_is_div_3_5_3(self):
        self.assertEqual(is_div_3_5(9), 3)

    def test_is_div_3_5_5(self):
        self.assertEqual(is_div_3_5(10), 5)

    def test_is_div_3_5_not_div(self):
        self.assertEqual(is_div_3_5(19), None)

    @parameterized.expand([
        (45, 35),
        (9, 3),
        (10, 5),
        (19, None)
    ])
    def test_is_div_3_5(self, n, expected):
        self.assertEqual(is_div_3_5(n), expected)


def test_is_div_3_5_example():
    assert is_div_3_5(25) == 5


@pytest.mark.parametrize('n, expected', [
    (45, 35),
    (9, 3),
    (10, 5),
    (19, None)
])


def test_is_div_3_5(n, expected):
    assert is_div_3_5(n) == expected


@pytest.mark.parametrize('numbers', [
    [1, 3, 8, 1.54, 9, 13],
    ['salutari'],
    [1 + 2j, 7]
])
def test_only_ints(numbers):
    with pytest.raises(NotIntegerNumberException):
        only_ints(numbers)
