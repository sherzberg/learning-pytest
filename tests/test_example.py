import pytest


def test_addition():
    assert 5 + 2 == 7


def f():
    raise SystemExit(1)


def test_raises():
    with pytest.raises(SystemExit):
        f()
