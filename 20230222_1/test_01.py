
def multiply(a, b):
    # 将需要测试的片段, 标准格式，需要运行的代码前面加 >> >, 相当于进入cmd这种交互环境执行，期望的结果前面不需要加 >>>
    # 放到multiply函数的注释里
    """
    function: 两个数相乘
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """

    return a * b


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
