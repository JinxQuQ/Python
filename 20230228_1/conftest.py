import pytest


@pytest.fixture(scope="session")
def start():
    print("\n打开首页")
    return "yoyo"
