def open_and_close_file(file_path):
    """Открывает и закрывает файл

    Args:
        file_path: путь до файла
    """
    f = open(file_path, 'r')
    f.close()
