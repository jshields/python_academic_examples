#!/bin/python
# jshields

#import os, sys
import codecs

#from  import 

#TODO

class FontAwesome(object):
	__init__:
		pass

	def read():
		f = codecs.open('fontawesome_chars.rst', encoding='utf-8', mode='r')
		for line in f:
		    print repr(line)

	def symbol(name):
		# return unicode character specified by name string
		return ur''
