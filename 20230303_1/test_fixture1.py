import pytest


@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    b = "123456"
    return (a, b)


def test_1(user):
    u = user[0]
    p = user[1]
    print("测试账号：%s, 密码：%s" % (u, p))
    assert u == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_fixture1.py"])
