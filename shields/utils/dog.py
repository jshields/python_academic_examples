#!/bin/python
# jshields


from animal import Animal


class Dog(Animal):
	def __init__(self, name, breed, color):
		self.species = u'canine'
		try:
			self.name = unicode(name, 'utf_8', strict)
		except ValueError:
			logging.critical('Non-Unicode String passed as name')
		self.breed = unicode(breed, 'utf_8', replace)
		self.color = unicode(color, 'utf_8', replace)

	@classmethod
	def __str__:
		return u'This is a %s %s %s' % (species, breed, color)

	@classmethod
	def emoji:
		# dog emoji
		return ur'\u1F436'.encode('unicode_escape')



"""
#convert to unicode
teststring = unicode(teststring, 'utf-8')
#encode it with string escape
teststring = teststring.encode('unicode_escape')
"""
