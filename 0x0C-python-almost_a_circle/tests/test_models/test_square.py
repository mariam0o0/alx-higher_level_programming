#!/usr/bin/python3
"""Unittests for base"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unit test for Square model"""

    def setUp(self):
        self.square = Square(10, 3, 5, 1)

    def test_constructor(self):
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 5)
        self.assertEqual(self.square.id, 1)

    def test_str(self):
        self.assertEqual(str(self.square), "[Square] (1) 3/5 - 10")

    def test_update_args(self):
        self.square.update(2, 20, 6, 8)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 6)
        self.assertEqual(self.square.y, 8)
        self.assertEqual(self.square.id, 2)

    def test_update_kwargs(self):
        self.square.update(size=20, x=6, y=8, id=2)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 6)
        self.assertEqual(self.square.y, 8)
        self.assertEqual(self.square.id, 2)

    def test_to_dictionary(self):
        expected_dict = {'id': 1, 'x': 3, 'size': 10, 'y': 5}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
