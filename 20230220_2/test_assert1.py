def f():
    return 3


def test_function():
    assert f() == 4

# 断言f()函数的返回值，接下来会看到断言失败，因为返回的值是3，判断等于4，所以失败了
# 从报错信息可以看到断言失败原因：E assert 3 == 4
