import time
from math import factorial


def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """

    def wrapper(arg1):
        start = time.time()
        resource = function(arg1)
        end = time.time() - start
        print(end)
        return resource

    return wrapper


@time_execution
def fact(num):
    return factorial(num)


fact(10000)
