from datetime import date


class Person:
    count = 0  # class variable/attribute
    MIN_YEAR = 1920

    def __init__(self, name, date_of_birth: date):
        self.name = name  # instance variable/attribute
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: date):
        if value.year < self.MIN_YEAR:
            raise ValueError(f"Invalid date of birth: {value}")
        self._date_of_birth = value

    @property
    def age(self):
        return self.years_since(self.date_of_birth)

    def __str__(self):
        return f"{self.name} ({self.date_of_birth})"

    def __repr__(self):
        return f"<{self.__class__.__name__} object at {id(self)}>"

    def __lt__(self, other: "Person"):
        return self.date_of_birth > other.date_of_birth

    def __le__(self, other: "Person"):
        return self.date_of_birth >= other.date_of_birth

    def greet(self, greeting):  # instance method
        print(f"{greeting.capitalize()}, I am {self.name}!")

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def years_since(date_start: date):
        today = date.today()
        years = today.year - date_start.year
        if (date_start.month, date_start.day) > (today.month, today.day):
            years -= 1
        return years


if __name__ == "__main__":
    p1 = Person("Anna", date(2003, 6, 13))
    print(p1, repr(p1), p1.__dict__, Person.__bases__)
    p2 = Person("John", date(1984, 7, 6))

    p1.name = "Jane"

    if p1 < p2:
        print(f"{p1.name} is younger than {p2.name}")

    p1.greet("hello")
    p2.greet("hi")

    print(Person.count, p1.count, p1.count is Person.count)

    print(Person.years_since(date(2024, 11, 20)))
    print(Person.years_since(date(2022, 11, 20)))

    try:
        p1.date_of_birth = date(1910, 6, 12)  # should not work
    except ValueError as ex:
        print(ex)
    try:
        p3 = Person("Jimmy", date(1910, 6, 12))
    except ValueError as ex:
        print(ex)

    print(p1.age)
