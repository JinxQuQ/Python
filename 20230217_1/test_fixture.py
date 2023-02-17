# 新建一个文件test_fixt.py
# coding:utf-8
import pytest


# 不带参数时默认scope="function"
@pytest.fixture()
# 如果@pytest.fixture()里面没有参数，那么默认scope=”function”，也就是此时的级别的function，针对函数有效
def login():
    print("输入账号，密码先登录")


def test_s1(login):
    print("用例1：登录之后其它动作111")


def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")


def test_s3(login):
    print("用例3：登录之后其它动作333")


if __name__ == "__main__":
    pytest.main(["-s", "test_fix.py"])



