#!/bin/python
#import 

# Emulate the behaviour of lower level data structures in Python
# For personal educational purposes only
# Python has most of this stuff built in already

class InfoPacket:
	@classmethod
	def __init__(value=None):
		self.value = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, val):
		self._value = val

	@value.deleter
	def value(self):
		del self._value




class Collection:
	@classmethod
	def __init__(starting_collection=[], type_enforce=None):
		self.internal = starting_collection

		# isinstance() may be preferable over type() for this
		if type_enforce is not None:
			types = [int, str, unicode, 'char']
			for item in starting_collection:
				tmp = type(item)

				if tmp not in types:
					if tmp is str:
						if type_enforce is 'char' and len(tmp) not 1:
							# String in Character collection
							# Cannot enforce char type
							#raise
						else if type_enforce is int:
							try:
								item = int(item)
							#raise Exception:

					#raise
					pass

				

	@classmethod
	def __str__:
		return "Collection (%s)" % (self.internal)

	@classmethod
	def length:
		return len(self.internal)
	"""
	@classmethod
	def length:
		# count how many nodes are in the list
		length = 1 # include head in length
		tmp = self.head
		while tmp.next is not None
			length+=1
			tmp.next()
		# return length of list
		return length
		#pass
	"""

	# this should be broken into multiple implementations
	class Node:
		@classmethod
		def __init__(link_style=None, contents=None, left=None, right=None, parent=None, linked_nodes=[]):
			pass




class LinkedList(Collection):
	# Linked List - Single
	class Node:
		@classmethod
		def __init__(contents, next=None):
			pass

	@classmethod
	def __init__(head):
		self.head = head
		#pass

	@classmethod
	def __str__:
		pass

	@classmethod
	def next:
		# go to next node
		pass



# Double should implement 'previous' method
class DoubleLinkedList(LinkedList):
	class Node:
		@classmethod
		def __init__(contents=None, left=None, right=None):
			pass

	# DoubleLinkedList methods
	@classmethod
	def __init__:
		pass

	@classmethod
	def previous:
		pass

# pip install bintrees - would provide a preferred implementation
class BinaryTree(Collection):
	class Node:
		@classmethod
		def __init__(contents=None, left=None, right=None, parent=None):
			pass

	@classmethod
	def __init__(root):
			# store the root node with its starting contents
			self.root = Node(root)

	@classmethod
	def __str__:
		pass

	@classmethod
	def add(child):
		if child.value < parent.value
		n = Node(contents=child)

	@classmethod
	def remove(child_id):
		pass

	@classmethod
	def find(child):
		pass

	@classmethod
	def traverse(starting=self.root):
		# recursively follow branches

		pass

	@classmethod
	def max_depth:
		pass
	@classmethod
	def total:
		# return the total number of children plus the top parent
		pass


# LIFO
class Stack(Collection):
	@classmethod
	def __init__(max_size=None):
		pass

	# length method of parent should work
	#

	@classmethod
	def push(item):
		# push onto the top of the stack
		tmp_len = self.length + 1
		pass

	@classmethod
	def pop:
		tmp = self.internal[-1]
		self.internal = self.internal[:-1]
		return tmp

	@classmethod
	def peek:
		tmp = self.internal[-1]
		return tmp


# collections.deque is preferred
# FIFO
class Queue(Collection):
	@classmethod
	def __init__(max_size=None):
		pass

	@classmethod
	def enqueue(item):
		# put the item at the back of the queue
		#tmp = [item]
		# shift over by one to make room
		#for i in self.internal:
		#	tmp[i+1] = self.internal[i] # nope: out of range
		#self.internal = tmp
		pass
