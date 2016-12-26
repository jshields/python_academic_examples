#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for basic_oo_example"""
import logging
import unittest
from unittest import TestCase
from python_utils.basic_oo_example.animal import Animal
from python_utils.basic_oo_example.dog import Dog
from python_utils.basic_oo_example.cat import Cat


class TestAnimal(TestCase):
    """Tests for basic_oo_example.animal Animal"""

    def setUp(self):
        # create an Animal to test
        self.bigfoot = Animal('Bigfoot', 'unknown', 'brown')

    def tearDown(self):
        del self.bigfoot

    def test_stringRepresentations(self):
        # repr and str are qualitatively different
        self.assertFalse(repr(self.bigfoot) is str(self.bigfoot))
        # but repr should still return something of type string
        self.assertTrue(type(repr(self.bigfoot)) is str)

    def test_emoji(self):
        # Animal's emoji should be the black-question-mark-ornament emoji
        self.assertEqual(self.bigfoot.__class__.emoji(), u'❓')

    def test_name(self):
        # make sure the parent's name property works on the parent
        self.assertEqual(self.bigfoot.name, 'Bigfoot')
        self.bigfoot.name = 'Sasquatch'
        self.assertEqual(self.bigfoot.name, 'Sasquatch')


class TestDog(TestCase):
    """Tests for basic_oo_example.dog Dog"""

    def setUp(self):
        # create a Dog to test
        self.rover = Dog('Rover', 'Great Dane', 'grey')

    def tearDown(self):
        del self.rover

    def test_stringRepresentations(self):
        # repr and str are qualitatively different
        self.assertFalse(repr(self.rover) is str(self.rover))
        # but repr should still return something of type String
        self.assertTrue(type(repr(self.rover)) is str)

    def test_speak(self):
        # make sure a string returns on speak
        bark = self.rover.speak()
        self.assertTrue(type(bark) is str)

    def test_emoji(self):
        # Dog's emoji should be the dog-face emoji
        self.assertEqual(self.rover.__class__.emoji(), u'🐶')

    def test_name(self):
        # make sure the parent's name property works on this child
        self.assertEqual(self.rover.name, 'Rover')
        self.rover.name = 'Champ'
        self.assertEqual(self.rover.name, 'Champ')


class TestCat(TestCase):
    """Tests for basic_oo_example.cat Cat"""

    def setUp(self):
        # create a Cat to test
        self.whiskers = Cat('Whiskers', 'Tabby', 'orange')

    def tearDown(self):
        del self.whiskers

    def test_stringRepresentations(self):
        # repr and str are qualitatively different
        self.assertFalse(repr(self.whiskers) is str(self.whiskers))
        # but repr should still return something of type string
        self.assertTrue(type(repr(self.whiskers)) is str)

    def test_speak(self):
        # make sure a string returns on speak
        meow = self.whiskers.speak()
        self.assertTrue(type(meow) is str)

    def test_emoji(self):
        # Cat's emoji should be the cat-face emoji
        # u prefix required because: u'\U0001f431' != '\xf0\x9f\x90\xb1'
        self.assertEqual(self.whiskers.__class__.emoji(), u'🐱')

    def test_name(self):
        # make sure the parent's name property works on this child
        self.assertEqual(self.whiskers.name, 'Whiskers')
        self.whiskers.name = 'Mittens'
        self.assertEqual(self.whiskers.name, 'Mittens')

    def test_scratch(self):
        # make sure that the cat scratch method returns a string
        scr = self.whiskers.scratch('the scratching post')
        self.assertTrue(type(scr) is str)


if __name__ == '__main__':
    unittest.main()
