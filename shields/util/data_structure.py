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
    def value(self, value):
       self._value = value

    @value.deleter
    def value(self):
       del self._value


class LinkedList(object):
    """single Linked List data structure"""
    
    class Node:
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
    class Node:
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

# pip install bintrees - would provide a preferred implementation


class BinaryTree(object):
    """Binary Tree"""

    class BinaryTreeRootException(Exception):
        """Exception related to the root Node"""
        pass

    class BinaryTreeNodeException(Exception):
        """Exception related to a Node"""
        def __init__(self, message):
            # super call the parent class constructor
            super(BinaryTreeNodeException, self).__init__(message)

            # a preset message
            self.insertErrorMsg = 'Attempted insertion of non-Node.'

    # nested Node class for use in BinaryTree class
    class Node(object):
        """Node for Binary Tree"""
        def __init__(self, parent=None, value=None, left=None, right=None):
            self._parent = parent

            if self._parent == None:
                self._isrootlike = True
            else:
                self._isrootlike = False

            self._value = value
            self._left = left
            self._right = right

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, value):

            if value == None:
                self._isrootlike = True
            else:
                self._isrootlike = False
                if not isinstance(value, Node):
                    raise BinaryTreeRootException('Cannot set root to instance other than of type Node.')

            self._parent = value
        

        @property
        def left(self):
            """get the node to the left"""
            return self._left

        @left.setter
        def left(self, value):
            """set the left Node"""
            if isinstance(value, Node):
                self._left = value
            else:
                raise BinaryTreeNodeException(BinaryTreeNodeException.insertErrorMsg)

        @property
        def right(self):
            """get the node to the right"""
            return self._right

        @right.setter
        def right(self, node_value):
            """set the right Node"""
            if isinstance(value, Node):
                self._right = value
            else:
                raise BinaryTreeNodeException(BinaryTreeNodeException.insertErrorMsg)

        # end Node class

    def __init__(self, root=None):
        """initialize Binary Tree"""
        # Node IDs
        self._ids = []
        # a Binary Tree must have at minimum a single root Node
        if (not isinstance(root, Node)) and (root != None):
            raise BinaryTreeRootException('Invalid root. Must be a Node.')
        if root == None:
            self._root == Node()
            # at index 0 insert 0
            self._ids.insert(0, 0)

    def root(self):
        """get the root Node / head"""
        return self._root
        

    #   def add(self, child):
    #       if child.value < parent.value
    #       n = Node(value=child)


    def remove(self, child_id):
       pass

    def find(self, node_value):
        # find node(s) by value and return their IDs
       pass

    @property
    def depth(self):
        pass
        #deepest = 0
        #for
        #return deepest

    def print_tree(self):
        """draw a visual representation of the tree"""
        #        o
        #       / \
        #      o   o
        #     / \ / \
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
       #tmp = [item]
       # shift over by one to make room
       #for i in self.internal:
       # tmp[i+1] = self.internal[i] # nope: out of range
       #self.internal = tmp
       pass

    def dequeue(self, item):
       pass



def main():
    """for during development only"""
    print('starting smoke test')

    import ipdb
    ipdb.set_trace()

    print(BinaryTree)
    print(BinaryTree.Node)

    bintree = BinaryTree(root=Node('root node val'))

    root = bintree.root

    root.left = Node('left node val')
    root.right = Node('right node val')

    root.left.left = Node('left left node val')
    root.left.right = Node('left right node val')




if __name__ == '__main__':
    main()
