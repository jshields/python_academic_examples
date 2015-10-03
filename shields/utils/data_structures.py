#!/bin/python
#import 

# Emulate the behaviour of lower level data structures in Python
# For personal educational purposes only
# Python has most of this stuff built in already

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
		while tmp.next_node is not None
			length+=1
			tmp.next()
		# return length of list
		return length
		#pass
	"""

	# this should be broken into multiple implementations
	class Node:
		@classmethod
		def __init__(link_style=None, contents=None, left_node=None, right_node=None, parent_node=None, linked_nodes=[]):
			#if link_style not in link_styles:
			#	raise InvalidNodeLink
			#self.link_style = link_style
			#self.contents = contents
			#self.left_node = left_node
			#self.right_node = right_node
			#self.parent_node = parent_node
			#self.linked_nodes = linked_nodes
			pass




class LinkedList(Collection):
	# Linked List - Single
	class Node:
		@classmethod
		def __init__(contents, right_node=None):
			#if link_style not in link_styles:
			#	raise InvalidNodeLink
			#self.link_style = link_style
			#self.contents = contents
			#self.left_node = left_node
			#self.right_node = right_node
			pass

	@classmethod
	def __init__(head):
		self.head = head
		#pass

	@classmethod
	def __str__:
		pass

	def assemble_from_python_list(lst):
		#ll = LinkedList()
		#for node_candidate in lst:
		#	n = Node(contents=node_candidate, next_node=)
		pass

	@classmethod
	def next:
		# go to next node
		pass



# Double should implement 'previous' method
class DoubleLinkedList(LinkedList):
	class Node:
		@classmethod
		def __init__(contents=None, left_node=None, right_node=None):
			#if link_style not in link_styles:
			#	raise InvalidNodeLink
			#self.link_style = link_style
			#self.contents = contents
			#self.left_node = left_node
			#self.right_node = right_node
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
		def __init__(contents=None, left_node=None, right_node=None, parent_node=None):
			#if link_style not in link_styles:
			#	raise InvalidNodeLink
			#self.link_style = link_style
			#self.contents = contents
			#self.left_node = left_node
			#self.right_node = right_node
			#self.parent_node = parent_node
			#self.linked_nodes = linked_nodes
			pass

	@classmethod
	def __init__(root):
		# self.Node or just Node?
		if type(root) is not self.Node:
			# raise
			pass
		elif root.parent_node is not None:
			# root cannot have a parent
			# raise
			pass
		else:
			self.root = root

	@classmethod
	def __str__:
		pass

	@classmethod
	def add(child, position):
		n = Node(contents=child)

	@classmethod
	def remove(child_id):
		pass

	@classmethod
	def find(child):
		pass

	@classmethod
	def traverse(starting_node=self.root):
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

	@classmethod
	def push(item):
		pass

	@classmethod
	def pop:
		pass

	@classmethod
	def peek:
		pass


# collections.deque is preferred
# FIFO
class Queue(Collection):
	@classmethod
	def __init__(max_size=None):
		pass
