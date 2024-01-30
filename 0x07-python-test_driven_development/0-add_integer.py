#!/usr/bin/python3
"""
Module add-integer
add two integers
"""


def add_integer(a, b=98):
	"""a function that adds 2 integers"""

	if not isinstance(a, (int,float)):
		raise TypeError("a must be an integer")
	if not isinstance(b, (int,float)):
		raise TypeError("b must be an integer")
	if isinstance(a,float):
		a = int(a)
	if isinstance(b,float):
		b = int(b)
	return a + b
