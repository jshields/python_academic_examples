#!/usr/bin/python
"""Tests for search algorithms"""
import unittest

from examples.search.linear import linear_search
from examples.search.binary import binary_search


# TODO fix mixed type list searching / sorting:
# changed in Python 3: TypeError: unorderable types: str() < int()


class TestSearch(unittest.TestCase):
    """Search unit tests"""

    def setUp(self):
        # self.fixture_jumbled_list = [5, 'x', 2, 'A', 'r', 'R', 'N', '3', 'K', 'l']
        self.fixture_jumbled_list = ['5', 'x', '2', 'A', 'r', 'R', 'N', '3', 'K', 'l']
        # [2, 5, '3', 'A', 'K', 'N', 'R', 'l', 'r', 'x']
        self.fixture_ordered_list = sorted(self.fixture_jumbled_list)
        self.fixture_jumbled_string = "sDdfXcsddVooVj7d476tTnrwDF#4uts6r"

    def test_linear_search(self):
        """Test linear search algorithm"""
        result = linear_search('not in list', self.fixture_jumbled_list)
        self.assertFalse(result)

        result = linear_search('x', self.fixture_jumbled_list)
        # 'x' is at index 1
        self.assertEqual(result, 1)

    def test_binary_search(self):
        """Test binary search algorithm"""
        result = binary_search('not in list', self.fixture_ordered_list)
        self.assertFalse(result)

        result = binary_search('x', self.fixture_ordered_list)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
