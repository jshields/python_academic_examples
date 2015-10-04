#!/usr/bin/python
# jshields
import logging
from animal import Animal

class Cat(Animal):
	"""Cat class, child of Animal"""

	_emoji = u'\U0001F431' # cat-face
	_sound = 'Meow!' # used by Animal's speak method

	def scratch(self, target):
		result = '%s the cat scratches %s' % (self.name, str(target))
		print(result)
		return result
