#!/usr/bin/python
"""
Emulate the behaviour of lower level data structures, in Python.
For personal educational purposes only.
Python has most of this stuff built in already.
"""
# jshields

class InfoPacket(object):

	def __init__(self, value=None):
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




class Collection(object):

	def __init__(self, collection=None, type_enforce=None):
		if collection is None:
			collection = []

		self.internal = collection

		# isinstance() may be preferable over type() for this
		if type_enforce is not None:
			types = [int, str, unicode, 'char']
			for item in collection:
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

				

	def __str__(self):
		return "<Collection (%s)>" % (self._items)

	@classmethod
	def length(self):
		return len(self._items)
	"""
	def length(self):
		# count how many nodes are in the list
		length = 1 # include head in length
		tmp = self.head
		while tmp.next is not None
			length+=1
			tmp.next()
		# return length of list
		return length
	"""

	# this should be broken into multiple implementations
	class Node(object):
		def __init__(self, link_style=None, contents=None, left=None, right=None, parent=None, linked_nodes=None):
			if linked_nodes is None:
				linked_nodes = []
			pass


class LinkedList(Collection):
	# Linked List - Single
	class Node:
		def __init__(contents, next=None):
			pass

	def __init__(self, head):
		self.head = head

	def next:
		# go to next node
		pass



# Double should implement 'previous' method
class DoubleLinkedList(LinkedList):
	class Node:
		def __init__(contents=None, left=None, right=None):
			pass

	# DoubleLinkedList methods
	def __init__(self):
		pass

	def previous(self):
		pass

# pip install bintrees - would provide a preferred implementation
class BinaryTree(Collection):
	class Node:
		def __init__(self, contents=None, left=None, right=None, parent=None):
			pass


	def __init__(self, root):
			# store the root node with its starting contents
			self.root = Node(root)



	def add(self, child):
		if child.value < parent.value
		n = Node(contents=child)


	def remove(self, child_id):
		pass


	def find(self, child):
		pass

	def traverse(self, starting=self.root):
		# recursively follow branches
		pass

	@property
	def max_depth(self):
		#deepest = 0
		#for
	    #return deepest
	

	def total(self):
		# return the total number of children plus the top parent
		pass


# LIFO
class Stack(Collection):
	"""Stack data structure implementation"""

	def __init__(self, max_size=None):
		self.max_size = max_size
		self.

	# length method of parent should work

	def push(self, item):
		# push onto the top of the stack
		# equivalent to append()
		pass

	def pop(self):
		# pop the top one off of the stack
		# equivalent to pop() method of the python list
		tmp = self._items[-1]
		self.internal = self._items[:-1]
		return tmp

	def peek(self):
		tmp = self._items[-1]
		return tmp


# collections.deque is preferred
# FIFO
class Queue(Collection):
	
	def __init__(self, max_size=None):
		pass

	def enqueue(self, item):
		# put the item at the back of the queue
		#tmp = [item]
		# shift over by one to make room
		#for i in self.internal:
		#	tmp[i+1] = self.internal[i] # nope: out of range
		#self.internal = tmp
		pass

	def dequeue(self, item):
		pass
