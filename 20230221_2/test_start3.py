import time
import pytest


# start设置scope为module级别，在当前.py用例模块只执行一次，autouse=True自动使用
@pytest.fixture(scope="module", autouse=True)
def start(request):
    print('\n-----开始执行module----')
    print('module      : %s' % request.module.__name__)
    print('----------启动浏览器---------')
    yield
    print("------------结束测试 end!-----------")


# open_home设置scope为function级别，每个用例前都调用一次，自动使用
@pytest.fixture(scope="function", autouse=True)
def open_home(request):
    print("function：%s \n--------回到首页--------" % request.function.__name__)


def test_01():
    print('-----------用例01--------------')


def test_02():
    print('-----------用例02------------')


if __name__ == "__main__":
    pytest.main(["-s", "test_start3.py"])
