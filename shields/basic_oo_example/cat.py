#!/bin/python
# jshields
import logging
from animal import Animal

class Cat(Animal):
	"""Cat class, child of Animal"""

	_species = u'feline'
	_emoji = ur'\u1F431' # cat-face

	def speak(self):
		"""Cat override for Animal.speak"""
		return 'Meow!'
