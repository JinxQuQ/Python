# test_fixture.py

import pytest


@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc111'


def test_fixture(fixtureFunc):
    print('我调用了222{}'.format(fixtureFunc))
    # .format   ——相当于+string


if __name__ == '__main__':
    pytest.main(['-v', 'test_fixture.py'])
