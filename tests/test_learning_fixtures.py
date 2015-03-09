import pytest


class MockClass(object):

    def add(self, x, y):
        return 5


@pytest.fixture
def mock_add():
    return MockClass()


def test_add(mock_add):
    result = mock_add.add(9, 9)

    assert result == 5
