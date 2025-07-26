#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 1]), 10)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-1, 0, 3, -5, 2]), 3)

    def test_all_same_numbers(self):
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.5, 2.8]), 3.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            max_integer("not a list")

    def test_list_with_string_element(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])


if __name__ == '__main__':
    unittest.main()
