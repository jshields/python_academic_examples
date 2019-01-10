#!/usr/bin/python
"""Tests for sort algorithms"""
import unittest

from examples.sort import bubble, insertion, merge, quick, selection


class TestSort(unittest.TestCase):
    """
    Sort unit tests

    These assertions are a bit precarious due to inline sorting algorithms
    which affect the same object we compare to,
    but should work to detect differences in sorting as compared to what is returned from
    the `sorted` function since it does not operate inline
    """

    def setUp(self):
        self.jumbled_int_lists = (
            [100, 3, 47, 14, 2, 5, 8, 32, 9, 10, 63, 33, 6, 2, 7, 8, 2, 3, 4, 5, 22, 78],
            [9, 3, 1, 6, 4, 7, 7, 2, 0],
            [0, 1, 3, 2, 4, 7, 7, 6, 9],
            [2, 6, 1, 7, 7, 7, 7, 3, 2],
            [5, 2, 3, 1, 4, 8, 5, 9],
            [5, 3, 5, 5, 5, 6, 8],
            [6, 3, 4, 1, 2, 7, 3],
            [0, 1, 2, 7, 0, 1, 2],
            [5, 3, 7, 1, 3, 2],
            [2, 6, 1, 7, 3, 2],
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

    def test_merge_sort(self):
        for lst in self.jumbled_int_lists:
            self.assertEqual(
                merge.merge_sort(lst),
                sorted(lst)
            )

    def test_bubble_sort(self):
        for lst in self.jumbled_int_lists:
            bubble.bubble_sort(lst)
            self.assertEqual(
                lst,
                sorted(lst)
            )

    def test_bubble_sort_optimized(self):
        for lst in self.jumbled_int_lists:
            # sort the list inline
            bubble.bubble_sort_optimized(lst)
            self.assertEqual(
                lst,
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
