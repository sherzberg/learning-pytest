import pytest


@pytest.mark.parametrize("input,expected", [
    (8, 8),
    (6, 6),
    (42, 42),
])
def test_simple(input, expected):
    assert input == expected
