import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Oleksiy','Nikolaenko', 5000)

    def test_give_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 10000)

    def test_give_custom_raise(self):
        self.employee.give_raise(30000)
        self.assertEqual(self.employee.salary, 35000)

unittest.main()