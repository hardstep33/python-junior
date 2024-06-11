from block_1.common import (
    MyException,
)


def ex(function):
    def wrap(arg1,arg2):
        try:
            return function(arg1,arg2)
        except Exception:
            raise MyException(Exception)

    return wrap


class Value:
    @ex
    def __init__(self, value):
        self.value_self = value

    @ex
    def __add__(self, other):
        return self.value_self + other

    @ex
    def __sub__(self, other):
        return self.value_self - other

    @ex
    def __mul__(self, other):
        return self.value_self * other

    @ex
    def __truediv__(self, other):
        return float(self.value_self) / other


# ten = Value(10)
# print(ten + 11)
# print(ten * 8)
# print(ten - 7)
# print(ten / 2)
