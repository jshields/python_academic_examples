from python_utils.util.data_structure.binary_tree import BinaryTree


def main():
    """for during development only"""
    print('starting smoke test')

    import ipdb;ipdb.set_trace()

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
