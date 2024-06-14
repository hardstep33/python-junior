from datetime import time, timedelta, datetime


class MathClock:
    def __init__(self):
        today = datetime.today()
        init_time = time(hour=0, minute=0)
        self.__value = datetime.combine(today, init_time)

    def get_time(self):
        return self.__value.strftime("%H:%M")

    def __add__(self, other):
        self.__value = self.__value + timedelta(minutes=other)

    def __sub__(self, other):
        self.__value = self.__value - timedelta(minutes=other)

    def __truediv__(self, other):
        self.__value = self.__value - timedelta(hours=other)

    def __mul__(self, other):
        self.__value = self.__value + timedelta(hours=other)
