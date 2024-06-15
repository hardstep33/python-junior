def contextmanager(function):
    def wrapper(arg1, arg2):
        func = function(arg1, arg2)
        print(len(list(func.readlines())))
        return func

    return wrapper


@contextmanager
def open_file(file_name, mode):
    return open(file_name, mode)


open_file("log.txt", "r")


class FileReader:
    def __init__(self, file_name, mode):
        self.__name = file_name
        self.__mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.__name, self.__mode)
        print(len(self.file.readlines()))
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with FileReader('log.txt', 'r') as f:
    print(f.closed)
