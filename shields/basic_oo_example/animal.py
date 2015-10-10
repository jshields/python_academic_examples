#!/bin/python
# jshields
import logging

logging.basicConfig(filename='animal.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

class Animal:
	def __init__(self, name, color):
		self.name = name
		self.species = None
		self.color = color
		_emoji = ur'\u2753' # ? black-question-mark-ornament
		logging.info("%s initialized" % self)

	def __str__(self):
		return u'<Animal name=%s color=%s >' % (self.name, self.color)

	# each animal subclass should set '_emoji' equal to a raw unicode string for the emoji representing their class
	@classmethod
	def emoji():
		return _emoji.encode('unicode_escape')
