#!/usr/bin/python3
"""Unittests for base"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unit test for Rectangle model"""
    
    def setUp(self):
        self.rect = Rectangle(10, 20, 3, 5, 1)

    def test_constructor(self):
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 20)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 5)
        self.assertEqual(self.rect.id, 1)

    def test_area(self):
        self.assertEqual(self.rect.area(), 200)

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (1) 3/5 - 10/20")

    def test_update_args(self):
        self.rect.update(2, 30, 40, 6, 8)
        self.assertEqual(self.rect.width, 30)
        self.assertEqual(self.rect.height, 40)
        self.assertEqual(self.rect.x, 6)
        self.assertEqual(self.rect.y, 8)
        self.assertEqual(self.rect.id, 2)

    def test_update_kwargs(self):
        self.rect.update(width=30, height=40, x=6, y=8, id=2)
        self.assertEqual(self.rect.width, 30)
        self.assertEqual(self.rect.height, 40)
        self.assertEqual(self.rect.x, 6)
        self.assertEqual(self.rect.y, 8)
        self.assertEqual(self.rect.id, 2)

    def test_to_dictionary(self):
        expected_dict = {'x': 3, 'width': 10, 'id': 1, 'height': 20, 'y': 5}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
