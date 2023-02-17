import pytest

# 如果其中一个用例出现异常，不影响yield后面的teardown执行,运行结果互不影响，并且在用例全部执行完之后，会呼唤teardown的内容
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行teardown!")
    print("最后关闭浏览器")


def test_s1(open):
    print("用例1：搜索python-1")

    # 如果第一个用例异常了，不影响其他的用例执行
    raise NameError  # 模拟异常


def test_s2(open):  # 不传login
    print("用例2：搜索python-2")


def test_s3(open):
    print("用例3：搜索python-3")


if __name__ == "__main__":
    pytest.main(["-s", "test_f1.py"])
