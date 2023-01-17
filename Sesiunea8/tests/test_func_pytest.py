import pytest
from Sesiunea8.app.func import is_div_3_5


def test_is_div_3_5_example():
    assert is_div_3_5(25) == 4


@pytest.mark.parametrize('n, expected', [
    (45, 35),
    (9, 3),
    (10, 5),
    (19, None)
])
def test_is_div_3_5(n, expected):
    assert is_div_3_5(n) == expected