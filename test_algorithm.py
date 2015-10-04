#!/usr/bin/python
"""Tests for search and sort algorithms"""
# jshields
import unittest
from unittest import TestCase

from shields.util.algorithm import Search, Sort


class TestSearch(TestCase):

	def setUp(self):
		self.fixture_jumble_list = [5, 'x', 2, 'A', 'r', 'R', 'N', '3', 'K', 'l']
		self.fixture_jumble_string = "sDdfXcsddVooVj7d476tTnrwDF#4uts6r"

	def tearDown(self):
		del self.fixture_jumble_list
		del self.fixture_jumble_string

	def test_linear(self):
		pass

	def test_binary(self):
		"""Test binary search algorithm"""
		#result = Search.binary('not in list', fixture_jumble_list)
		#assertFalse(result)
		pass
