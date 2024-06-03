def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    month_num = {
        'январь': 1,
        'февраль': 2,
        'март': 3,
        'апрель': 4,
        'май': 5,
        'июнь': 6,
        'июль': 7,
        'август': 8,
        'сентябрь': 9,
        'октябрь': 10,
        'ноябрь': 11,
        'декабрь': 12,
    }
    month_ind = month_num.get(month)
    if month_ind in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month_ind in [4, 6, 9, 11]:
        return 30
    elif month_ind == 2:
        return 28
    else:
        return 0
