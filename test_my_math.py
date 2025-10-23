# test_my_math.py
import unittest
from my_math import add, subtract

class TestMyMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, 3), -2)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -5), -5)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(10, -5), 15)
        self.assertEqual(subtract(-10, 5), -15)

if __name__ == '__main__':
    unittest.main() 