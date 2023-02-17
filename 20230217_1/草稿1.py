# def say_hello():
#     print("hello!")
#
#
# def say_goodbye():
#     print("goodbye!")  # bug here
#
#
# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()
#
# ----------------老板要求调用每个方法前都要记录进入函数的名称,方法1：-------------------------------------
#
# def say_hello():
#     print("[DEBUG]: enter say_hello()")
#     print("hello!")
#
#
# def say_goodbye():
#     print("[DEBUG]: enter say_goodbye()")
#     print("hello!")
#
#
# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()

# ------------------老板要求调用每个方法前都要记录进入函数的名称,方法2：------------------------------------
def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print("[DEBUG]: enter {}()".format(caller_name))


def say_hello():
    debug()
    print("hello!")


def say_goodbye():
    debug()
    print("goodbye!")


if __name__ == '__main__':
    say_hello()
    say_goodbye()