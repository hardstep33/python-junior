class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def __init__(self, *args):
        self.tuple = tuple(args)

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        item_list = list(self.tuple)
        return item_list.count(value)

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        item_list = list(self.tuple)
        result = None
        for idx, item in enumerate(item_list):
            if value == item:
                result = idx
                if result is not None:
                    return result
            else:
                continue

        if result is None:
            raise ValueError
        else:
            return result

    def __getitem__(self, item):
        return self.tuple[item]
