#!/bin/python
# jshields
import logging

logging.basicConfig(filename='animal.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

class Animal:
	def __init__(self, name, color):
		self.name = name
		self.species = None
		self.color = color
		logging.info("%s initialized" % self)

	def __str__(self):
		return u'<Animal name=%s color=%s >' % (self.name, self.color)
