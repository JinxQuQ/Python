import pytest


def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    # assert 属于手动断言/手动制造错误，有这个就会返回failed，方便调试
    # assert 0  # to see what was printed


if __name__ == "__main__":
    pytest.main(["-s", "test_case1.py"])
