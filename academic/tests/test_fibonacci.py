#!/usr/bin/python
"""Tests for fibonacci sequence"""
import unittest

from examples.fibonacci_sequence import (
    fibonacci_recurse,
    fibonacci_memoized,
    fibonacci_upto_num_dp,
)


class TestSearch(unittest.TestCase):
    """Search unit tests"""

    def setUp(self):
        self.real_fibs_to_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_fibonacci_recurse_real_fibs_to_10(self):
        for i in range(len(self.real_fibs_to_10)):
            result = fibonacci_recurse(i)
            self.assertEquals(result, self.real_fibs_to_10[i])

    def test_fibonacci_memoized_real_fibs_to_10(self):
        for i in range(len(self.real_fibs_to_10)):
            result = fibonacci_memoized(i)
            self.assertEquals(result, self.real_fibs_to_10[i])

    #def test_fibonacci_upto_num_dp_real_fibs_to_10(self):
    #    fibonacci_upto_num_dp()

if __name__ == '__main__':
    unittest.main()
