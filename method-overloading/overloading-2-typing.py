"""
@typing.overload
The @overload decorator allows describing functions and methods that support multiple different 
combinations of argument types. A series of @overload-decorated definitions must be followed by 
exactly one non-@overload-decorated definition (for the same function/method). 
The @overload-decorated definitions are for the benefit of the type checker only, since they will 
be overwritten by the non-@overload-decorated definition, while the latter is used at runtime but 
should be ignored by a type checker. At runtime, calling a @overload-decorated function directly 
will raise NotImplementedError
"""
from typing import overload


@overload
def func_1(x: int) -> int:
    pass


@overload
def func_1(x: str) -> str:
    pass


def func_1(x):
    # actual implementation of func_1
    if isinstance(x, int):
        return "I am func_1 with int"
    elif isinstance(x, str):
        return "I am func_1 with str"
    else:
        raise TypeError("func_1() takes int or str")


print(func_1(10))
print(func_1("hello"))
