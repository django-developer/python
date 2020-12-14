''' binary tree construction

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

class Node: 
    def __init__(self, val): 
        self.left = None
        self.right = None
        self.val = val 

    def build_tree_1(self, prefix, infix):

        if len(prefix) == 0:
            return None
        if len(prefix) == 1:
            return Node(prefix[0])

        root = Node(prefix[0])
        index = infix.index(root.val)
        root.left = self.build_tree_1(prefix[1 : index + 1], infix[:index])
        root.right = self.build_tree_1(prefix[index + 1:], infix[index + 1:])
        return root

    def build_tree_2(self, postfix, infix):

        if len(postfix) == 0:
            return None
        if len(postfix) == 1:
            return Node(postfix[-1])

        root = Node(postfix[-1])
        index = infix.index(root.val)
        root.left = self.build_tree_2(postfix[:index], infix[:index])
        root.right = self.build_tree_2(postfix[index:-1], infix[index + 1:])
        return root

    def bst_tree_1(self, prefix):

        infix = sorted(prefix)
        root = self.build_tree_1(prefix, infix)
        return root

    def bst_tree_2(self, postfix):

        infix = sorted(postfix)
        root = self.build_tree_2(postfix, infix)
        return root

    def pre_order(self, root, res=[]): 

        if root: 
            res += [root.val]
            self.pre_order(root.left, res) 
            self.pre_order(root.right, res)
        return(res)

    def in_order(self, root, res=[]): 

        if root: 
            self.in_order(root.left, res) 
            res += [root.val]
            self.in_order(root.right, res) 
        return(res)
          
    def post_order(self, root, res=[]): 

        if root: 
            self.post_order(root.left, res) 
            self.post_order(root.right, res) 
            res += [root.val]
        return(res)

if __name__ == '__main__':

    '''
    prefix = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]    # (Root, L, R)
    infix  = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]    # (L, Root, R)
    x = Node(None)
    root = x.build_tree_1(prefix, infix)

    postfix = [9, 1, 2, 12, 7, 5, 3, 11, 4, 8]      # (L, R, Root)
    infix   = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]
    x = Node(None)
    root = x.build_tree_2(postfix, infix)

    prefix = [20, 16, 5, 18, 17, 19, 60, 85, 70]
    x = Node(None)
    root = x.bst_tree_1(prefix)

    postfix = [5, 17, 19, 18, 16, 70, 85, 60, 20]
    x = Node(None)
    root = x.bst_tree_2(postfix)
    '''

    prefix = [20, 16, 5, 18, 17, 19, 60, 85, 70]
    x = Node(None)
    root = x.bst_tree_1(prefix)

    print('')
    print('pre_order traversal:  {}'.format(x.pre_order(root)))
    print('in_order traversal:   {}'.format(x.in_order(root)))
    print('post_order traversal: {}'.format(x.post_order(root)))
    print('')

