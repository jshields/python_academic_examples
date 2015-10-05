#!/usr/bin/python
"""Search and Sort algorithms"""
# jshields

import logging
import copy

logging.basicConfig(filename='algorithm.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

class SearchException(Exception):
	"""
	Exception class for this module.
	Does not override anything, simply provides a more specific name.
	"""
	pass

class Search(object):
	"""Search class acts as a library for searching algorithm methods"""

	@classmethod
	def linear(cls, item, lst):
		"""
		Linear search of a list for an item.
		Returns the first index of the item in a list.
		Will return False if nothing is found.
		"""
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
		"""
		Binary search for an item in an ordered list.
		Numbers > Capital Alpha > Lowercase Alpha.
		Returns an index in the list or False if not found.
		"""
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

class Sort(object):
	"""Sort class acts as a library for sorting algorithm methods"""

	@classmethod
	def _quicksort_partition(cls, lst, start, end):
		"""Internal partition and sorting method for Sort._quick driver method"""
		# the pivot element value will be the basis for comparison in sorting
		# we use the first item in this partition of the list as the pivot
		# the selection is arbitrary and the value could be anything, low or high
		# this is the pivot value
		pivot = lst[start]
		# for now the pivot element remains in its initial list position,
		# and elements following it will be index swapped (their indices switch)
		# relative to the pivot value, not the pivot's index

		# set the starting positions of the left and right brackets
		left = start+1
		right = end

		# keep swapping until the brackets pass/overlap each other
		swapping = True
		while swapping:
			# relative to the pivot value,
			# left bracket moves from left to right, and will trip on any element with a value not less than,
			# right bracket moves from right to left, and will trip on any element with a value not greater than
			while left <= right and lst[left] <= pivot:
				left = left + 1
			while lst[right] >= pivot and right >= left:
				right = right -1
			if right < left:
				swapping = False
			else:
				# swap places if the bracket trips
				logging.debug('_quicksort_partition swapping: %s with %s' % (lst[left], lst[right]))
				tmp=lst[left]
				lst[left]=lst[right]
				lst[right]=tmp
		# swap pivot with the last known right bracket (greater than) element
		# this puts the pivot in between the elements that were swapped to the "less than" position
		# and elements that were swapped to the "greater than" position
		logging.debug('_quicksort_partition final swap: %s with %s' % (lst[start], lst[right]))
		tmp=lst[start]
		lst[start]=lst[right]
		lst[right]=tmp
		# the end result is that all elements less than are left of the pivot element, potentially unsorted
		# and all elements greater than the pivot element are right of the pivot element, potentially unsorted
		# return the pivot index, so that the less than and greater than sides can be partitioned and sorted again,
		# in Sort._quick
		logging.debug('pivot is %s' % right)
		return right

	@classmethod
	def _quick(cls, lst, start, end):
		"""Quicksort implementation for a list, internal"""
		# this method is called recursively
		# on the left and right sections of each partition
		# the sorting work is done in _quicksort_partition

		# eventually, a recursion depth will be reached
		# at which the overall list is fully sorted
		if start < end:
			# sort before and after the pivot
			pivot_index = cls._quicksort_partition(lst, start, end)
			cls._quick(lst, start, pivot_index-1)
			cls._quick(lst, pivot_index+1, end)
		return lst

	@classmethod
	def quick(cls, src_lst, start=0, end=None, inline=False):
		"""
		Quicksort implementation for a list, external.
		Specify if inline sorting should be used with Boolean kwarg 'inline'
		"""
		# user specified kwargs take effect in this top level call
		# this way, recursive calls in the internals are not affected by user kwargs
		# by default sort all the way to the end of the list
		if end is None:
			end = (len(src_lst) - 1)

		# support for inline sorting vs returning a sorted copy
		if inline:
			lst = src_lst
		else:
			lst = copy.deepcopy(src_lst)
		return cls._quick(lst, start, end)

	@classmethod
	def merge(cls, lst):
		"""Merge sort implementation"""
		pass

	@classmethod
	def bubble(cls, lst):
		"""Bubble sort implementation"""
		swapping = True
		while swapping:
			swapping = False
			# because we look-ahead by 1 index, only iterate to length - 1
			for i in range(len(lst) - 1):
				# bigger/greater items should "bubble" to the top
				# if one item belongs where the other is,
				# swap them as part of the sort
				if lst[i] > lst[i+1]:
					swapping = True
					# swap the items
					tmp = lst[i]
					lst[i] = lst[i+1]
					lst[i+1] = tmp
		return lst

	@classmethod
	def insertion(cls, src_lst, start=0, end=None, inline=False):
		"""Insertion sort implementation"""
		# support for inline sorting vs returning a sorted copy
		if inline:
			lst = src_lst
		else:
			lst = copy.deepcopy(src_lst)

		if end is None:
			end = len(lst)

		# because we look-behind by 1 index, start iteration at length + 1
		for i in range(start + 1, end):
			value = lst[i]
			cursor = i - 1

			logging.debug('insertion: for looping, index at %d, current value %s, cursor at %d' %\
																(i, value, cursor))

			# while the elements behind the current element are of greater value,
			# push the current element backwards
			while lst[cursor] > value and cursor >= 0:
				# starting from the element of current 'value',
				# swap values with the element that the cursor is looking back towards,
				# falling through the rest of the list behind the current element
				logging.debug('insertion: while looping, shifting index of %s up by one' % lst[cursor])
				lst[cursor + 1] = lst[cursor]
				cursor -= 1
				logging.debug('insertion: while looping, cursor at %d' % cursor)
			# finally, insert the 'value' back into the list
			logging.debug('insertion: out of while, inserting %s back into the list at index %d' %\
																	(lst[cursor + 1], (cursor + 1)))
			lst[cursor + 1] = value

		return lst
