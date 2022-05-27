from functools import singledispatch


"""
To define a generic function, decorate it with the @singledispatch decorator. When defining a 
function using @singledispatch, note that the dispatch happens on the type of the first argument.
"""


@singledispatch
def func_1(name, number):
    print(f"I am func_1 with name:{name} and number:{number}")


"""
To add overloaded implementations to the function, use the register() attribute of the generic 
function, which can be used as a decorator. For functions annotated with types, the decorator 
will infer the type of the first argument automatically.
"""


@func_1.register(int)
def _(number):
    print(f"I am register to func_1 with number:{number}")


"""
The below method should not be defined, as the dispatcher acts on the first argument of the function
The call func_1("hello", 10) will raise an TypeError: _() takes 1 positional argument but 2 were give
"""
# @func_1.register(str)
# def _(name):
#     print(f"I am register to func_1 with name:{name}")


func_1("Hello", 10)  # I am func_1 with name:Hello and number:10
func_1(10)  # I am register to func_1 with number:10
func_1("Hello")  # TypeError: _() takes 1 positional argument but 2 were given
