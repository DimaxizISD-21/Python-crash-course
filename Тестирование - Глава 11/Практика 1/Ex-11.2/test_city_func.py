import unittest
from city_func import value_country

class TestCase_functions(unittest.TestCase):
    def test_value(self):
        result = value_country('ukraine', 'vasylkiv')
        self.assertEqual(result, 'Ukraine, Vasylkiv')

    def test_value_population(self):
        result = value_country('ukraine', 'vasylkiv', 4000000)
        self.assertEqual(result, 'Ukraine, Vasylkiv, Population: 4000000')

unittest.main()