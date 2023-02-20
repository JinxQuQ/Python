import pytest

# 为了写关于引发异常的断言，可以使用pytest.raises作为上下文管理器，如下

# 2.ZeroDivisionError：除数为0.
# >>> 1/0
#
# Traceback (most recent call last):
# File"", line 1, in ZeroDivisionError: division by zero
#
# 任何一个数值被零除都会导致ZeroDivisionError异常。


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
