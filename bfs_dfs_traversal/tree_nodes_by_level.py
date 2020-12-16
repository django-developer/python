''' binary tree nodes by level

    note:
        - we need prefix or postfix to get the next root node info while
          constructing the binary tree
        - once we know the root, to get the left sub tree and right sub tree
          we need infix

        - binary search tree: left tree nodes < root node < right tree nodes
        - infix = sorted(prefix or postfix) because
          infix is always in the ascending order for a binary search tree

    build_tree_1(prefix, infix)     # build binary tree given prefix, infix
    build_tree_2(postfix, infix)    # build binary tree given postfix, infix
    bst_tree_1(prefix)              # build binary search tree given prefix
    bst_tree_2(postfix)             # build binary search tree given postfix
    get_directed_tree(self, root)   # returns dict of adjacency sets
                                    # for a directed tree given the root
    get_undirected_tree(self, directed_tree)    # convert directed to
                                                # undirected

    bfs(self, undirected_tree, start_node)  # output:
                                            # dict of sets
                                            # (level, set of nodes at that level)

    dfs(self, undirected_tree, start_node, T = defaultdict(set), P = set(), i = 0):

                                            # note: uses preorder dfs
                                            # output:
                                            # dict of sets
                                            # (level, set of nodes at that level)


'''

class Node: 

    from collections import defaultdict


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

    def get_directed_tree(self, root, T = defaultdict(set)):

        if root:
            tmp = root.val
            if (tmp) not in T:
                if root.left:
                    T[tmp].add(root.left.val)
                if root.right:
                    T[tmp].add(root.right.val)

            self.get_directed_tree(root.left, T) 
            self.get_directed_tree(root.right, T)

        return(T)

    def get_undirected_tree(self, directed_tree):

        from copy import deepcopy

        T = deepcopy(directed_tree)

        for u in T.keys():
            for v in T[u]:
                T[v].add(u)

        return(T)

    def bfs(self, undirected_tree, start_node):

        T = {}
        s = start_node

        if not len(undirected_tree): return(T)
        if start_node not in undirected_tree: return(T)

        P = set()   # already processed
        Q = set()   # to be processed

        i = 0
        Q.add(s)

        while Q:
            T[i] = Q
            i = i+1
            tmp = set()
            for v in Q:
                tmp.update(undirected_tree[v].difference(P))
            P.update(Q)
            Q = tmp
        return(T)

    def dfs(self, undirected_tree, start_node, T = defaultdict(set), P = set(), i = 0):

        s = start_node

        if not len(undirected_tree): return(T)
        if start_node not in undirected_tree: return(T)

        Q = set()
        Q.update(undirected_tree[s].difference(P))
        P.add(s)
        T[i].add(s)

        if not Q: return(T)
        i = i+1
        for v in Q:
            self.dfs(undirected_tree, v, T, P, i)

        return(T)

if __name__ == '__main__':

    prefix = [20, 16, 5, 18, 17, 19, 60, 85, 70]
    x = Node(None)
    root = x.bst_tree_1(prefix)

    print('pre_order traversal:  {}'.format(x.pre_order(root)))
    print('in_order traversal:   {}'.format(x.in_order(root)))
    print('post_order traversal: {}'.format(x.post_order(root)))

    print('')
    directed_tree = x.get_directed_tree(root)
    print('directed tree (dict of adjacency sets): {}'.format(directed_tree))

    print('')
    undirected_tree = x.get_undirected_tree(directed_tree)
    print('undirected tree (dict of adjacency sets): {}'.format(undirected_tree))

    print('')
    root = 18
    bfs = x.bfs(undirected_tree, root)
    print('nodes by level from root({}) using bfs: {}'.format(root, bfs))

    print('')
    root = 18
    dfs = x.dfs(undirected_tree, root)
    print('nodes by level from root({}) using preorder dfs: {}'.format(root, dfs))


