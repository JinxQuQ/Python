# test_03.py
# coding:utf-8
import pytest

# 如果用到@pytest.fixture，里面用2个参数情况，可以把多个参数用一个字典去存储，这样最终还是只传一个参数
# 不同的参数再从字典里面取对应key值就行，如： user = request.param[“user”]

# 测试账号数据
test_user_data = [{"user": "admin1", "psw": "111111"},
                  {"user": "admin1", "psw": ""}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("登录账户：%s" % user)
    print("登录密码：%s" % psw)
    if psw:
        return True
    else:
        return False


# indirect=True 声明login是个函数
# 如果要用到login里面的返回值，def test_login(login)时，传入login参数，函数返回值就是login了
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    # 登录用例
    a = login
    print("测试用例中login的返回值:%s" % a)
    assert a, "失败原因：密码为空"


if __name__ == "__main__":
    pytest.main(["-s", "test_03.py"])
