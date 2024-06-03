def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение
    C = (F - 32) * 5/9
    F = C * 9/5 + 32
    Returns: значение как результат конвертации
    """
    if to_scale == 'C':
        return (value - 32) * 5 / 9
    elif to_scale == 'F':
        return value * 9 / 5 + 32
    else:
        return value
