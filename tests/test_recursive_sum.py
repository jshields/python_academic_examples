#!/usr/bin/python
import unittest
from examples.recursive_sum import recursive_sum


class TestRecursiveSum(unittest.TestCase):

    def test_recursive_sum_empty(self):
        self.assertEqual(
            recursive_sum([]),
            0
        )

    def test_recursive_sum_single_positive(self):
        self.assertEqual(
            recursive_sum([1]),
            1
        )

    def test_recursive_sum_single_negative(self):
        self.assertEqual(
            recursive_sum([-1]),
            -1
        )

    def test_recursive_sum_misc(self):
        # FIXME break into multiple tests
        self.assertEqual(
            recursive_sum([-2, -4]),
            -6)
        self.assertEqual(
            recursive_sum([-2, 3]),
            1)
        self.assertEqual(
            recursive_sum([-2, -3, 5]),
            0)
        self.assertEqual(
            recursive_sum([1, 2, 4]),
            7)
        self.assertEqual(
            recursive_sum([0, 1, 2, 4, 40]),
            47)


if __name__ == '__main__':
    unittest.main()
