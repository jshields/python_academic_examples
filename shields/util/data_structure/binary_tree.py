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
        # Node IDs sequence
        self._ids = []
        # a Binary Tree must have at minimum a single root Node
        if (not isinstance(root, Node)) and (root != None):
            raise BinaryTreeRootException('Invalid root. Must be a Node.')
        if root == None:
            self._root == Node()
        else:
            self._root = root

    def root(self):
        """get the root Node / head"""
        return self._root
        

    #   def add(self, child):
    #       if child.value < parent.value
    #       n = Node(value=child)


    def remove(self, child_id):
       pass

    def find_nodes_by_value(self, node_value):
        """find node ids with an exact match to a specific value"""
        #found_nodes = []
        # find node(s) by value and return their IDs
        #found_nodes.append(id(found_node))
        #return found_nodes
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
