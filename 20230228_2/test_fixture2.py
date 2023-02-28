import pytest


@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    return a


def test_1(user):
    assert user == "yoyo111"  # 用例失败就是failed


if __name__ == "__main__":
    pytest.main(["-s", "test_fixture2.py"])
