import pytest


@pytest.fixture()
# 定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()，fixture命名不要用test开头，跟用例区分开。用例才是test开头的命名。
def user():
    print("获取用户名")
    a = "yoyo"
    # fixture是可以有返回值的，如果没return默认返回None。用例调用fixture的返回值，直接就是把fixture的函数名称当成变量名称，如下案例
    return a


def test_1(user):
    assert user == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_fixture1.py"])
