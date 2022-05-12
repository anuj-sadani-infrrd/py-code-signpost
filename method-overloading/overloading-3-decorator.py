from collections import defaultdict


function_table = defaultdict(dict)


def overload(arg_types=(), kwarg_types=()):
    def determine_types(args, kwargs):
        return tuple([type(a) for a in args]), tuple(
            [(k, type(v)) for k, v in kwargs.items()]
        )

    def wrapper(func):
        named_func = function_table[func.__name__]
        named_func[arg_types, kwarg_types] = func
        print(named_func)

        def call_function_by_signature(*args, **kwargs):
            if named_func.get(determine_types(args, kwargs)) is None:
                raise NotImplementedError("No implementation for this signature")
            return named_func[determine_types(args, kwargs)](*args, **kwargs)

        return call_function_by_signature

    return wrapper


@overload((int,))
def func_1(x: int):
    print("I am func_1 with int")


@overload((str,))
def func_1(x: str):
    print("I am func_1 with str")


@overload((str,), (("foo", int),))
def func_1(x: str, foo: int):
    print("I am func_1 with str and foo")


func_1(10)  # I am func_1 with int
func_1("hello")  # I am func_1 with str
func_1("hello", foo=10)  # I am func_1 with str and foo
func_1(10, foo=10)  # NotImplementedError: No implementation for this signature
