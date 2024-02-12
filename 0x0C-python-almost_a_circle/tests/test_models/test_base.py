#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Define unit test for Base model"""

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty(self):
        self.assertEqual(Base.to_json_string([{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]),
                          '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

class TestCreateMethod(unittest.TestCase):
    def test_create_rectangle(self):

        rect = Rectangle.create(width=10, height=20)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)

    def test_create_square(self):
        square = Square.create(size=5)
        self.assertEqual(square.size, 5)


if __name__ == '__main__':
    unittest.main()
