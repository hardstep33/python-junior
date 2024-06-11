counter_num = 0


def counter(function):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    def wrap():
        global counter_num
        res = function
        counter_num += 1
        return counter_num

    return wrap


