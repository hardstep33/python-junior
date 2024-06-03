def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    list_numbers = []
    for i in range(1000, 2001):
        if i % 7 == 0 and i % 5 != 0 and i != 0:
            list_numbers.append(i)
        else:
            continue

    return list_numbers
