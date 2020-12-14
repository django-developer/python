
'''binary tree construction

    binary tree:
        - we need prefix or postfix
          to get the next root node info while constructing the binary tree
        - once we know the root, we need infix
          to get the left sub tree and right sub tree

    binary search tree:
        - left sub tree nodes < root node < right sub tree nodes
        - infix = sorted(prefix or postfix) because
          infix is always in the ascending order for a binary search tree

    build_tree_1(prefix, infix)     # build binary tree given prefix, infix
    build_tree_2(postfix, infix)    # build binary tree given postfix, infix
    bst_tree_1(prefix)              # build binary search tree given prefix
    bst_tree_2(postfix)             # build binary search tree given postfix

'''
