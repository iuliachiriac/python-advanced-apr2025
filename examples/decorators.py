import functools


def make_pretty(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):  # inner -> functools.wraps(func)(inner)
        print("I got decorated")
        return func(*args, **kwargs)

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name):
    print(f"Hello, {name}!")


@make_pretty
def decrement(nr, step=1):
    """Decrements nr by step and returns the result"""
    return nr - step


# ordinary = make_pretty(ordinary)  # make_pretty.<locals>.inner
ordinary()

greet("Anna")

result = decrement(10, step=2)
print("Decrement result:", result)

help(decrement)
print("Function name:", decrement.__name__)
print("Function docstring:", decrement.__doc__)
