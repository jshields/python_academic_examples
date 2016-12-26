#!/usr/bin/python
"""
Emulate the behaviour of lower level data structures, in Python.
For educational purposes only.
Python has most of this stuff built in already.
"""


class InfoPacket(object):

    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value


class LinkedList(object):
    """single Linked List data structure"""

    class Node(object):
        """individual node within a Linked List"""
        def __init__(value, next_node=None):
            """initialize a node"""
            # value could be anything, including an object
            self.value = value
            self.next_node = next_node

    def __init__(self, items=None, head):
        """initialize LinkedList"""
        if items is None:
            items = []

        if type(items) != list:
            logging.warning('Non-list passed into Collection. May not function as intended.')

        self._items = items
        self.head = head

    def next:
        # go to next node
        pass


class DoubleLinkedList(object):
    """"""
    class Node(object):
        """A node in a doubly linked list"""
        def __init__(value=None, left=None, right=None):
            pass

    # DoubleLinkedList methods
    def __init__(self):
        pass

    def next:
        """go to next node"""
        pass

    def previous(self):
        """go to previous node"""
        pass


# LIFO
class Stack(Collection):
    """Stack data structure implementation"""

    def __init__(self, items, max_size=None):
        self.max_size = max_size

    # length method of parent class should work

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
        # tmp = [item]
        # shift over by one to make room
        # for i in self.internal:
        # tmp[i+1] = self.internal[i] # nope: out of range
        # self.internal = tmp
        pass

    def dequeue(self, item):
        pass
