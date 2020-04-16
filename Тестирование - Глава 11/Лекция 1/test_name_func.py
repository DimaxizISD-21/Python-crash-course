import unittest
from name_func import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('oleksiy', 'nikolaenko')
        self.assertEqual(formatted_name, 'Oleksiy Nikolaenko')

    def test_middle_name(self):
        formatted_name = get_formatted_name('oleksiy', 'nikolaenko', 'dimax')
        self.assertEqual(formatted_name, 'Oleksiy Nikolaenko Dimax')
        
unittest.main()

