import time
import pytest


@pytest.fixture(scope="function")
def start(request):
    print('\n-----开始执行function----')


def test_a(start):
    print("-------用例a执行-------")


class Test_aaa():

    def test_01(self, start):
        print('-----------用例01--------------')

    def test_02(self, start):
        print('-----------用例02------------')


if __name__ == "__main__":
    pytest.main(["-s", "test_06.py"])
