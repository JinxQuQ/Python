import pytest


@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app


def test_something_quick():
    pass


def test_another():
    pass


class TestClass:
    def test_method(self):
        pass

    def test_method1(self):
        assert 0


if __name__ == "__main__":
    pytest.main(["-s", "test_server.py", "-m=webtest"])
    # 实测：在pycharm中以"test_server.py::TestClass::test_method"，"-m=webtest"等方式指定运行某些用例均无效，用cmd运行有效
    # pytest.main(["-v", "test_server.py::TestClass::test_method"])
