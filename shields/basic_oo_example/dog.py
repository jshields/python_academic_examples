#!/usr/bin/python
# jshields
from animal import Animal

class Dog(Animal):
	"""Dog class, child of Animal"""

	_emoji = u'\U0001F436' # dog-face
	_sound = 'Woof!' # used by Animal's speak method
