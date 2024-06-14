class Multiplier:
    mult = 1

    def __init__(self, value):
        self.__value = value * self.mult

    @staticmethod
    def convert_to_mult(other):
        return other.get_value() if isinstance(other, Multiplier) else other

    def __add__(self, other):
        return Multiplier(self.__value + self.convert_to_mult(other))

    def __truediv__(self, other):
        return Multiplier(self.__value / self.convert_to_mult(other))

    def __mul__(self, other):
        return Multiplier(self.__value * self.convert_to_mult(other))

    def __sub__(self, other):
        return Multiplier(self.__value - self.convert_to_mult(other))

    def get_value(self):
        return self.__value


class Hundred(Multiplier):
    """Множитель на 100"""
    mult = 100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    mult = 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""
    mult = 1000000


# hundr = Hundred(10)
# th = Thousand(10)
# res = th + hundr
# print(res.get_value())
