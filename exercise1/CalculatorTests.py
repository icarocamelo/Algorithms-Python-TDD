import unittest

from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        expected = 4
        a = 2
        b = 2
        calc = Calculator()
        result = calc.sum(a, b)
        self.assertEqual(result, expected, 'it\'s wrong')

    def test_sum_with_one_letter_and_one_number(self):
        calc = Calculator()
        self.assertRaises(ValueError, calc.sum, 2, 'three')

    def test_sum_with_two_letters(self):
        calc = Calculator()
        self.assertRaises(ValueError, calc.sum, 'two', 'three')

if __name__ == '__main__':
    unittest.main()
