import pytest


@pytest.mark.repeat(5)
def test_001():
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-sv', __file__])
