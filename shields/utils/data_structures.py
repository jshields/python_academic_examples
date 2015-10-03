#!/bin/python
#import 

# Emulate the behaviour of lower level data structures in Python
class DataStructure:
	@classmethod
	def __init__:
		pass

	@classmethod
	def __str__:
		pass

	def assemble_from_python_list(lst):
		pass

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




class LinkedList(DataStructure):
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
	def len:
		# count how many nodes are in the list
		length = 1 # include head in length
		tmp = self.head
		while tmp.next_node is not None
			length+=1
			tmp.next()
		# return length of list
		return length
		#pass

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


class BinaryTree:
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
		self.root = root

	@classmethod
	def __str__:
		pass

	@classmethod
	def max_depth:
		pass
	@classmethod
	def total_nodes:
		pass

