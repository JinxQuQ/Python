import pytest

# 测试账号数据
test_user = ["admin1", "admin2"]
test_psw = ["11111", "22222"]


@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user


@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw


# 用例上面是可以同时放多个fixture的，也就是多个前置操作，可以支持装饰器叠加，使用parametrize装饰器叠加时，用例组合是2个参数个数相乘
# 如果参数user有2个数据，参数psw有2个数据，那么组合起来的案例是两个相乘，也就是组合2*2 = 4个用例
@pytest.mark.parametrize("input_user", test_user, indirect=True)
@pytest.mark.parametrize("input_psw", test_psw, indirect=True)
def test_login(input_user, input_psw):
    # 登录用例
    a = input_user
    b = input_psw
    print("测试数据a-> %s， b-> %s" % (a, b))
    assert b


if __name__ == "__main__":
    pytest.main(["-s", "test_04.py"])
