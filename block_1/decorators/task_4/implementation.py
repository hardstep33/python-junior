import time
from block_1.common import (
    MyException,
)


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def decorator_internal(function):
        def wrap():
            for i in range(1, times + 1):
                try:
                    return function()
                except Exception:
                    if i < times:
                        time.sleep(delay)
                    else:
                        raise MyException(Exception)

        return wrap

    return decorator_internal
