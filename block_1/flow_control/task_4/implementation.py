from datetime import (
    date,
)


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    try:
        date1 = date(some_date.year + 1, 1, 1)
        if (date1 - some_date).days == 1:
            return date1

        date2 = date(some_date.year, some_date.month + 1, 1)
        if (date2 - some_date).days == 1:
            return date2

        date3 = date(some_date.year, some_date.month, some_date.day + 1)
        if (date3 - some_date).days == 1:
            return date3

    except:
        return some_date
