# LEGB:
# Local
# Enclosing
# Global
# Built-in

# list = []  # shadowing of a built-in name
chars = list("hello")


def my_func(a):
    b = 0
    # chars = ""  # shadowing of a global name
    print(chars)
    print(a, b)


my_func(10)
