from block_1.common import (
    factorial,
    MyException,
)

cache_arr = {}


def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """

    def wrapper(arg):
        if isinstance(arg, int) and arg >= 0:
            return function(arg)
        else:
            raise MyException

    return wrapper


def cache(function):
    global cache_arr

    def wrapper(arg):
        if cache_arr.get(arg) is not None:
            print("return from cache")
            return cache_arr[arg]
        else:
            print("return from function")
            result = function(arg)
            cache_arr[arg] = result
            return result

    return wrapper


# @check_value
# @cache
# def new_factorial(arg):
#     return factorial(arg)
#
#
# print(new_factorial(100))
# print(new_factorial(1000))
# print(new_factorial(10000))
# print(new_factorial(10000))
# print(new_factorial(10000))
# print(new_factorial(10000))
# print(new_factorial(10000))
# print(new_factorial(10000))
# print(new_factorial(10000))
