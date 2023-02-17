import pytest


@pytest.fixture()
def login():
    print("输入账号，密码先登录")
    yield
    print("执行teardown!")
    print("最后关闭浏览器")