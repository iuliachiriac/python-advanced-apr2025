import pytest

from employee import Employee, BankAccount


@pytest.fixture
def bank_account():
    return BankAccount("ING", 1000)


@pytest.fixture
def employee(bank_account):
    return Employee("John Addams", bank_account, 100)


def test_create_employee():
    emp = Employee("Jane Doe", None, 100)
    assert emp.name == "Jane Doe"
    assert emp.salary == 100


@pytest.mark.parametrize("percent", (0, 3, 22, 50, 81, 104))
def test_invalid_percent(employee, percent):
    with pytest.raises(ValueError):
        employee.raise_salary(percent)


@pytest.mark.parametrize("percent,salary", [(5, 105), (10, 110), (20, 120)])
def test_valid_percent(employee, percent, salary):
    employee.raise_salary(percent)
    assert employee.salary == salary
