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
            [5, 3, 5, 5, 5, 6, 8],
            [6, 3, 4, 1, 2, 7, 3],
            [5, 3, 7, 1, 3, 2],
            # some edge cases
            [1, 1, 1, 1, 1],
            [2, 2, 2, 0],
            [1, 0],
            [0, 1],
            [5]
        )

    def test_quick_sort1(self):
        for lst in self.jumbled_int_lists:
            self.assertEqual(
                quick.QuickSort.quick(lst),
                sorted(lst)
            )

    def test_quick_sort2(self):
        for lst in self.jumbled_int_lists:
            self.assertEqual(
                quick.QuickSortMiddlePivot.quick(lst),
                sorted(lst)
            )


    @unittest.skip('Not Implemented')
    def test_merge_sort(self):
        for lst in self.jumbled_int_lists:
            self.assertEqual(
                merge.merge_sort(lst),
                sorted(lst)
            )

    def test_bubble_sort(self):
        for lst in self.jumbled_int_lists:
            self.assertEqual(
                bubble.bubble_sort(lst),
                sorted(lst)
            )

    def test_insertion_sort(self):
        for lst in self.jumbled_int_lists:
            self.assertEqual(
                insertion.insertion_sort(lst),
                sorted(lst)
            )

    def test_selection_sort(self):
        for lst in self.jumbled_int_lists:
            self.assertEqual(
                selection.selection_sort(lst),
                sorted(lst)
            )


if __name__ == '__main__':
    unittest.main()
