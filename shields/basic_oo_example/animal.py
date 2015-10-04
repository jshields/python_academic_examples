#!/usr/bin/python
# jshields
import logging

logging.basicConfig(filename='animal.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

class Animal(object):
	"""Base class for animals."""

	_emoji = u'\u2753' # black-question-mark-ornament
	_sound = '...'

	def __init__(self, name, breed, color):
		self._name = name
		self._breed = breed
		self._color = color

		logging.info("%s initialized" % self)

	def __repr__(self):
		return u'<Class %s name=%s breed=%s color=%s emoji=%s >' % (self.__class__.__name__,
													self._name, self._breed, self._color,
													self._emoji.encode('unicode_escape'))

	def __str__(self):
		return u'%s the %s %s' % (self._name, self._color, self._breed)

	def speak(self):
		"""Speak method should in some way describe the sound an animal makes.
		Children should define their _sound or override."""
		try:
			print(self._sound)
			return self._sound
		except AttributeError:
			raise Exception('No _sound defined for this animal! (%s)' % self)

	@property
	def name(self):
	    return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@classmethod
	def emoji(cls):
		"""Each Animal subclass should set '_emoji' equal to a unicode character
		representing their class"""
		return cls._emoji
