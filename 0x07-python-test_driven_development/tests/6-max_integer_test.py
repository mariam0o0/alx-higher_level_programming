#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for integers"""

    def test_max_integer(self):
        """Cases"""
        self.assertEqual(max_integer([8, 14, 3]), 14)
        self.assertEqual(max_integer([22, -5, -8, -17]), 22)
        self.assertEqual(max_integer([5, 15, -10]), 15)
        self.assertEqual(max_integer([-20, -15, -3]), -3)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([4, 30, 11]), 30)
        self.assertEqual(max_integer([987654, 34567, -123]), 987654)
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
