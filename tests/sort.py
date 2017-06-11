#!/usr/bin/python
"""Tests for sort algorithms"""
import unittest
from unittest import TestCase

from examples.sort import bubble, insertion, merge, quick, selection


class TestSort(TestCase):
    """Sort unit tests"""

    def setUp(self):
        self.jumbled_int_lists = (
            [9, 3, 1, 6, 4, 7, 7, 2, 0],
            [5, 2, 3, 1, 4, 8, 5, 9],
            [6, 3, 4, 1, 2, 7, 3],
            [5, 3, 7, 1, 3, 2],
            # some edge cases
            [1, 1, 1, 1, 1],
            [2, 2, 2, 0],
            [1, 0],
            [0, 1],
            [5]
        )

    def test_quick_sort(self):
        for lst in jumbled_int_lists:
            self.assertEqual(
                quick.QuickSort1.quick(lst),
                sort(lst)
            )

    def test_merge_sort(self):
        #self.assertEqual(
        #    merge.merge_sort(jumbled_int_list),
        #    sort(jumbled_int_list)
        #)
        pass

    def test_bubble_sort(self):
        for lst in jumbled_int_lists:
            self.assertEqual(
                bubble.bubble_sort(lst),
                sort(lst)
            )

    def test_insertion_sort(self):
        for lst in jumbled_int_lists:
            self.assertEqual(
                insertion.insertion_sort(lst),
                sort(lst)
            )

    def test_selection_sort(self):
        for lst in jumbled_int_lists:
            self.assertEqual(
                selection.selection_sort(lst),
                sort(lst)
            )


if __name__ == '__main__':
    unittest.main()
