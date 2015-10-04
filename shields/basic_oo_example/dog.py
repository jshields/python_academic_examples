#!/bin/python
# jshields
import logging
from animal import Animal

class Dog(Animal):
	"""Dog class, child of Animal"""

	_species = u'canine'
	_emoji = ur'\u1F436' # dog-face

	def speak(self):
		"""Dog override for Animal.speak"""
		return 'Woof!'
