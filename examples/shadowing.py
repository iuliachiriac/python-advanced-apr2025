# LEGB:
# Local
# Enclosing
# Global
# Built-in

# list = []  # shadowing of a built-in name
chars = list("hello")


def my_func(a):
    b = 0
    print(chars)
    print(a, b)


my_func(10)
