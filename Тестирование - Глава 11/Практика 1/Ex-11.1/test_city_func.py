import unittest
from city_func import value_country

class TestCase_functions(unittest.TestCase):
    def test_value(self):
        result = value_country('ukraine', 'vasylkiv')
        self.assertEqual(result, 'Ukraine, Vasylkiv')

unittest.main()