class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance=0):
        self.bank_name = bank_name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsException('insufficient funds')
        self._balance -= amount

    def __str__(self):
        return f"Bank: {self.bank_name} | Balance: {self._balance}"

    def __repr__(self):
        return self.__str__()


class Employee:
    ACCEPTED_RAISE_VALUES = (5, 10, 20)

    def __init__(self, name: str, bank_account: BankAccount, salary: int = 0):
        self.name = name
        self._bank_account = bank_account
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def raise_salary(self, percent: int):
        """method accepts one of these values (5, 10, 20) as percent"""
        if percent not in self.ACCEPTED_RAISE_VALUES:
            raise ValueError(f'Invalid raise value: {percent}%')
        self._salary += (percent / 100) * self._salary

    def receive_salary(self):
        self._bank_account.deposit(self._salary)

    @property
    def net_worth(self):
        return self._bank_account.balance

    def spend(self, amount):
        self._bank_account.withdraw(amount)
