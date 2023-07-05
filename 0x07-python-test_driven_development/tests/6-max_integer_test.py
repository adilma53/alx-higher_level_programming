#!/usr/bin/python3
""" test max integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ ----------- """

    def test_with_int(self):
        "" - ---------- """
        list = [1, 2, 5, 200]
        output = max_integer(list)
        self.assertEqual(output, 200)

    def test_with_float(self):
        "" ----------- """
        list = [0.4, 50.7, 50.9]
        output = max_integer(list)
        self.assertEqual(output, 50.9)

    def test_with_string(self):
        "" - ---------- """
        list = ['a', 'b', 1]
        self.assertRaises(TypeError, max_integer, list)

    def test_it_empty(self):
        "" ----------- """
        list = []
        output = max_integer(list)
        self.assertEqual(output, None)

    def test_as_not_list(self):
        "" - ---------- """
        list = 9
        self.assertRaises(TypeError, max_integer, list)

    def test_as_unique(self):
        "" ----------- """
        list = [23]
        output = max_integer(list)
        self.assertEqual(output, 23)

    def test_with_same_value(self):
        "" - ---------- """
        list = [9, 9, 9]
        output = max_integer(list)
        self.assertEqual(output, 9)

    def test_with_none(self):
        "" ----------- """
        self.assertRaises(TypeError, max_integer, None)

    def string_test(self):
        "" ----------- """
        list = ['man', 'woman']
        output = max_integer(list)
        self.assertEqual(output, 'man')


if __name__ == '__main__':
    unittest.main()
