import unittest

from ex_7_4_access_control_property import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John Doe", None, 1000)

    def test_raise_salary_valid_percent(self):
        for value_in, value_out in zip((5, 10, 20), (1050, 1100, 1200)):
            with self.subTest(percent=value_in, salary=value_out):
                self.setUp()
                self.employee.raise_salary(value_in)
                self.assertEqual(self.employee.salary, value_out)

    def test_raise_salary_invalid_percent(self):
        with self.assertRaises(ValueError):
            self.employee.raise_salary(50)
        self.assertEqual(self.employee.salary, 1000)

    @unittest.skip
    def test_skipped(self):
        pass
