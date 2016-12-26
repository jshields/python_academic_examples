#!/usr/bin/python
"""Tests for search and sort algorithms"""
import unittest
from unittest import TestCase

from python_utils.util.algorithm import Search, Sort


class TestSearch(TestCase):
    """Search unit tests"""

    def setUp(self):
        self.fixture_jumbled_list = [5, 'x', 2, 'A', 'r', 'R', 'N', '3', 'K', 'l']
        self.fixture_ordered_list = sorted(self.fixture_jumble_list)  # [2, 5, '3', 'A', 'K', 'N', 'R', 'l', 'r', 'x']
        self.fixture_jumbled_string = "sDdfXcsddVooVj7d476tTnrwDF#4uts6r"

    def tearDown(self):
        del self.fixture_jumble_list
        del self.fixture_ordered_list
        del self.fixture_jumble_string

    def test_linear(self):
        """Test linear search algorithm"""
        result = Search.linear('not in list', self.fixture_jumbled_list)
        self.assertFalse(result)
        result = Search.binary('x', self.fixture_jumbled_list)
        # 'x' is at index 1
        self.assertEqual(result, 1)

    def test_binary(self):
        """Test binary search algorithm"""
        result = Search.binary('not in list', self.fixture_ordered_list)
        self.assertFalse(result)
        result = Search.binary('x', self.fixture_ordered_list)
        self.assertEqual(result, 9)
