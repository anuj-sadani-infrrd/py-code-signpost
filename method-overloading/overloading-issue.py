"""function overloading simply does not work in Python"""


def foo(x: int):
    print("I am foo with int")


def foo(
    x: str,
):  # <-- this is the cause, the method in the global namespace is overwritten
    print("I am foo with str")


foo(1)  # I am foo with str
foo("hello")  # I am foo with str


def bar(x: int):
    print("I am bar with 1 argument")


def bar(x: int, y: int):
    print("I am bar with 2 arguments")


bar(1, 2)  # I am bar with 2 arguments
bar(1)  # TypeError: bar() missing 1 required positional argument: 'y'
