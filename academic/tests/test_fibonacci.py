#!/usr/bin/python
"""Tests for fibonacci sequence"""
import unittest

from examples.fibonacci_sequence import (
    fibonacci_recurse,
    fibonacci_memoized,
    fibonacci_bottom_up,
    fibonacci_upto_num_dp,
)


class TestSearch(unittest.TestCase):
    """Search unit tests"""

    def setUp(self):
        self.real_fibs_to_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_fibonacci_recurse(self):
        for i in range(len(self.real_fibs_to_10)):
            result = fibonacci_recurse(i)
            self.assertEqual(result, self.real_fibs_to_10[i])

    def test_fibonacci_memoized(self):
        for i in range(len(self.real_fibs_to_10)):
            result = fibonacci_memoized(i)
            self.assertEqual(result, self.real_fibs_to_10[i])

    def test_fibonacci_bottom_up(self):
        for i in range(len(self.real_fibs_to_10)):
            result = fibonacci_bottom_up(i)
            self.assertEqual(result, self.real_fibs_to_10[i])

    def test_fibonacci_upto_num_dp(self):
        self.assertEqual(
            fibonacci_upto_num_dp(0),
            [self.real_fibs_to_10[0]]
        )
        # both copies of 1 are returned with n of 1
        self.assertEqual(
            fibonacci_upto_num_dp(1),
            [0, 1, 1]
        )
        self.assertEqual(
            fibonacci_upto_num_dp(3),
            self.real_fibs_to_10[:5]
        )
        self.assertEqual(
            fibonacci_upto_num_dp(13),
            self.real_fibs_to_10[:8]
        )
        self.assertEqual(
            fibonacci_upto_num_dp(57),
            self.real_fibs_to_10
        )


if __name__ == '__main__':
    unittest.main()
