def flatten_list(matrix: list) -> list:
    """
    Преобразует матрицу (список списков) в линейный список.

    Args:
         matrix: список, элементами которого являются списки

    Returns:
        линейный список
    """
    return [x for y in matrix for x in y]
