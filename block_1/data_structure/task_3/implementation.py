def copy_dict(origin_dict):
    """
    Функция возвращает копию словаря.
    Рекурсивно копирует вложенные списки, словари, кортежи, множества.
    Проверяется тип входных данных и в зависимости от типа множества происходит цикл копирования.
    Внутри цикла в каждой итерации проверяется тип значения, и если тип - множество,
     запускает эту же функцию рекурсивно.
    """
    new_dict = {}
    if isinstance(origin_dict, dict):
        new_dict = {}
        for key, val in origin_dict.items():
            if not isinstance(val, (list, dict, tuple, set)):
                new_dict[key] = val
            else:
                new_dict[key] = copy_dict(val)
    elif isinstance(origin_dict, list):
        new_dict = []
        for val in origin_dict:
            if not isinstance(val, (list, dict, tuple, set)):
                new_dict.append(val)
            else:
                new_dict.append(copy_dict(val))
    elif isinstance(origin_dict, tuple):
        new_list = []
        for val in origin_dict:
            if not isinstance(val, (list, dict, tuple, set)):
                new_list.append(val)
            else:
                new_list.append(copy_dict(val))
        new_dict = tuple(new_list)
    elif isinstance(origin_dict, set):
        new_list = []
        for val in origin_dict:
            if not isinstance(val, (list, dict, tuple, set)):
                new_list.append(val)
            else:
                new_list.append(copy_dict(val))
        new_dict = set(new_list)

    return new_dict
