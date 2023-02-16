import pytest


# setup_function/teardown_function  每个用例开始和结束调用一次
def setup_function():
    print("setup_function：开始执行一条用例啦")


def teardown_function():
    print("teardown_function：执行完一条用例啦")


def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x
    # true


def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')
    # false


def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b
    # true


# 在 if __name__ == 'main': 下的代码只有在文件作为脚本直接执行的情况下才会被执行，而import到其他脚本中是不会被执行的
if __name__ == "__main__":
    # main()函数如果不带任何参数，那么执行的效果跟我们在cmd直接运行pytest命令一样，默认运行的是当前目录及子目录的所有文件夹的测试用例。
    # -s：显示程序中的print / logging输出。
    # -v：丰富信息模式, 输出更详细的用例执行信息。
    # -k：运行包含某个字符串的测试用例。如：pytest -k add XX.py表示运行XX.py中包含add的测试用例。
    # -q：简单输出模式, 不输出环境信息。
    # -x：出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
    pytest.main(["-q", "test_fixt_setup_function.py"])
# -s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程
