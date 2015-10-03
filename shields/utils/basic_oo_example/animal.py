#!/bin/python
# jshields
import logging

logging.basicConfig(filename='animal.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

class Animal():
	def __init__(self):
		self.species = None
		self.name = None
		self.living = True

	@classmethod
	def __str__:
		return u'generic animal'
