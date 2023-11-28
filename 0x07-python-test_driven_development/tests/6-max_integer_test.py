#!/usr/bin/python3

"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unittest class for max_integer
    """

    def test_module_docstring(self):
        """
        Test function for module docstring.
        """
        module = __import__('6-max_integer').__doc__
        self.assertTrue(len(module) > 1)

    def test_function_docstring(self):
        """
        Function to test for function docstring.
        """
        function = max_integer.__doc__
        self.assertTrue(len(function) > 1)

    def test_empty_list(self):
        """Test if list is empty.
        """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test if list contains single element.
        """
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)

    def test_positive_integers(self):
        """Test for positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, 8, 7, 5]), 9)

    def test_negative_integers(self):
        """Test for positive integers.
        """
        self.assertEqual(max_integer([-10, -38, -46, -25]), -10)
        self.assertEqual(max_integer([-60, -30, -40, -20, -80]), -20)

    def test_mixed_positive_negative(self):
        """Test for positive and negative integers.
        """
        self.assertEqual(max_integer([-19, 37, -46, 25]), 37)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_mixed_integers_and_floats(self):
        """Test for positive/negative integers and floats.
        """
        self.assertEqual(max_integer([1, 2.5, 3, 4.75]), 4.75)
        self.assertEqual(max_integer([-1.5, -2.5, 2, 6.8, 6.52]), 6.8)
        self.assertEqual(max_integer([10, -10, 10]), 10)
        self.assertEqual(max_integer([{1, 9}, {2}, {3}]), {1, 9})
        self.assertEqual(max_integer([1.5, 2.75, 3.25]), 3.25)

    def test_list_of_strings(self):
        """Test for positive/negative integers and floats.
        """
        self.assertEqual(max_integer("6789"), '9')
        self.assertEqual(max_integer("abcxyz"), 'z')
        self.assertEqual(max_integer(['a', 'b', 'c', 'x', 'y', 'z']), 'z')
        self.assertEqual(max_integer(["abc", 'x']), 'x')

    def test_string_elements(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c", 44, 63])


if __name__ == '__main__':
    unittest.main()

"""run test with python3 -m unittest -v tests.6-max_integer_test"""