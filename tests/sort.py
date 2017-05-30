#!/usr/bin/python
"""Tests for sort algorithms"""
import unittest
from unittest import TestCase

from examples.sort import Sort


# TODO
class TestSort(TestCase):
    """Sort unit tests"""

    def setUp(self):
        self.jumbled_int_list = [5, 2, 3, 1, 4, 8, 5, 9]

    def test_quick_sort(self):
        self.assertEqual(
            Sort.quick(),
            sort(jumbled_int_list)
        )


if __name__ == '__main__':
    unittest.main()
