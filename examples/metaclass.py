from abc import abstractmethod
from abc import ABCMeta


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"Initializing class {name}")
        super().__init__(name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print(f"Metaclass called for {cls} with {args} and {kwargs}")
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class MyOtherClass(metaclass=MyMeta):
    pass


class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        pass


my_instance = MyClass(10, b=20)
try:
    MyABC()
except TypeError as ex:
    print(ex)
