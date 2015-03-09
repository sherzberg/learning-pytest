import pytest


class SuperSweetMock():

    def first(self):
        return 0

    def second(self):
        return 1


@pytest.fixture(scope='module')
def supersweetmock():
    return SuperSweetMock()
