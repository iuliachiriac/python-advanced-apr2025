from datetime import date


class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.name} ({self.date_of_birth})"

    def __repr__(self):
        return f"<{self.__class__.__name__} object at {id(self)}>"

    def __lt__(self, other: "Person"):
        return self.date_of_birth > other.date_of_birth

    def __le__(self, other: "Person"):
        return self.date_of_birth >= other.date_of_birth


if __name__ == "__main__":
    p1 = Person("Anna", date(2003, 6, 13))
    print(p1, repr(p1), p1.__dict__, Person.__bases__)
    p2 = Person("John", date(1984, 7, 6))

    if p1 < p2:
        print(f"{p1.name} is younger than {p2.name}")

