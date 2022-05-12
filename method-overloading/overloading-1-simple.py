"""
Function overloading with default arguments and arguments unpacking works in Python
However there are some limitations to the usage of this feature
"""


def func_1(x: int, y: int = None):
    # Need to assign a default and add some conditional logic
    # cons:
    # Need to have default values and some business logic
    # additionally, the order of the arguments is important to avoid a syntax error
    # say: "def func_e(x=10, y): pass" # SyntaxError: non-default argument follows default argument
    if y is None:
        return x
    return x + y


def func_2(*args):
    # Need to unpack the arguments
    # cons:
    # Hard to control the order of the arguments (without extra code)
    # The args can be more than we expect, say the method should sum only two arguments
    result = 0
    for arg in args:
        result += arg
    return result


print(func_1(10))  # 10
print(func_1(10, 20))  # 30
print(func_2(10))  # 10
print(func_2(10, 20, 30))  # 60
