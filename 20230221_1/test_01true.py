import pytest

# 对登录的账号密码进行参数化
canshu = [{"user": "admin", "psw": "111"}]


# 把登录写为前置操作
@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("正在操作登录，账号：%s, 密码：%s" % (user, psw))
    if psw:
        return True
    else:
        return False


# 多个用例放到一个类中
@pytest.mark.parametrize("login", canshu, indirect=True)
class Test_xx:
    # test_01，test_02， test_03全部调用fixture里面的login功能

    def test_01(self, login):
        # 用例1登录
        result = login
        print("用例1：%s" % result)
        assert result == True
        # assert的意思是：满足assert后面的语句，TRUE即为通过，FALSE为失败

    @pytest.mark.xfail
    # 可以直接用该装饰器标记方法，表示期望该方法被标记为xfail，用例会正常执行，只是失败时不再显示堆栈信息，最终的结果有两个：用例执行失败时（XFAIL：符合预期的失败）、用例执行成功时（XPASS：不符合预期的成功）
    def test_02(self, login):
        result = login
        print("用例2,登录结果：%s" % result)
        # test_02和test_03执行前用if判断登录的结果，登录失败就执行，pytest.xfail(“登录不成功, 标记为xfail”)
        # 固定用法
        # if not ...:
        #     pytest.xfail("失败原因")——标记该用例失败，不予继续执行，并且说明失败原因
        if not result:
            pytest.xfail("登录不成功, 标记为xfail")

        assert 1 == 1
        # TRUE

    def test_03(self, login):
        result = login
        print("用例3,登录结果：%s" % result)
        # test_02和test_03执行前用if判断登录的结果，登录失败就执行，pytest.xfail(“登录不成功, 标记为xfail”)
        if not result:
            pytest.xfail("登录不成功, 标记为xfail")

        assert 1 == 1
        # TRUE


if __name__ == "__main__":
    pytest.main(["-s", "test_01true.py"])
