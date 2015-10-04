#!/usr/bin/python
"""Search and Sort algorithms"""
# jshields

class SearchException(Exception):
	"""Exception class for this module.
	Does not override anything, simply provides a more specific name."""
	pass

class Sort(object):

	def __init__(self):
		pass

	def bubble(self):
		pass
		# bubble sort

class Search(object):
	"""Search algorithms"""
	def __init__(self):
		pass

	@classmethod
	def linear(cls, item, lst):
		"""Linear search of a list for an item.
		Returns the first index of the item in a list.
		Will return False if nothing is found."""
		pos = 0
		while pos < len(lst):
			if lst[pos] is item:
				return pos
			pos+=1
		# opted for False rather than -1
		# simply because -1 is a valid list index in Python
		return False

		# real way to do this:
		#try:
		#	return lst.index(item)
		#except ValueError:
		#	return False

	@classmethod
	def binary(cls, item, lst):
		"""Binary search for an item in an ordered list.
		Numbers > Capital Alpha > Lowercase Alpha.
		Returns an index in the list or False if not found."""
		tmp = sorted(lst)
		if lst != tmp:
			raise SearchException('Search Error: Unsorted list passed to binary search.\
								 Please sort list so returned index will be meaningful.')

		bottom = 0
		top = len(tmp)-1
		while bottom <= top:
			# 
			middle = (bottom + top) // 2
			# middle, greater half or lesser half?
			if lst[middle] is item:
				# we found it
				return middle
			elif lst[middle] < item:
				# the item is greater than where we are looking
				# move the search bracket up
				bottom = middle + 1
			elif lst[middle] > item:
				# the item is less than where we are looking
				# move the search bracket down
				top = middle - 1
			else:
				raise SearchException('item not comparable to list.')
		return False
