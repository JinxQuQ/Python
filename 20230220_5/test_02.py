import pytest

# 测试账号数据
test_user_data = ["admin1", "admin2"]


# 如果想把登录操作放到前置操作里，也就是用到@pytest.fixture装饰器，传参就用默认的request参数
# user = request.param 这一步是接收传入的参数，本案例是传一个参数情况
@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("登录账户：%s" % user)
    return user


# 添加indirect=True参数是为了把login当成一个函数去执行，而不是一个参数
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    # 登录用例
    a = login
    print("测试用例中login的返回值:%s" % a)
    assert a != ""


if __name__ == "__main__":
    pytest.main(["-s", "test_02.py"])
