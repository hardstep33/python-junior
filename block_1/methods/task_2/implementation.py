from block_1.common import (
    MyException,
)


class ClassFather:
    _name = 'ClassFather'
    registered_list = {}

    @classmethod
    def get_name(cls):
        if cls._name == 'ClassFather' or cls.registered_list.get(cls._name) is None:
            raise MyException
        else:
            return cls._name

    @classmethod
    def register(cls):
        if cls._name != 'ClassFather':
            cls.registered_list[cls._name] = True
        else:
            raise MyException


class User1(ClassFather):
    _name = 'User1'


class User2(ClassFather):
    _name = 'User2'
