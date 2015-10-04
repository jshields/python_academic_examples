#!/bin/python
# jshields
import logging

logging.basicConfig(filename='animal.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

class Animal:
	"""Base class for animals."""

	_species = u'unknown'
	_emoji = ur'\u2753' # ? black-question-mark-ornament

	def __init__(self, name, breed, color):
		self._name = name
		self._breed = breed
		self._color = color

		logging.info("%s initialized" % self)

	def __str__(self):
		return u'<Class %s name=%s species=%s color=%s >' % (self.__class__.__name__,
																				self._name, self._species,
																				self._color) #emoji=%s self.emoji()

	def speak(self):
		"""Speak method should in some way describe the sound an animal makes.
		Children should override."""
		pass

	@property
	def name(self):
	    return self._name

	@name.setter
	def name(self, value):
		self._name = value

	# each animal subclass should set '_emoji' equal to a raw unicode string for the emoji representing their class
	@classmethod
	def emoji():
		return _emoji.encode('unicode_escape')
