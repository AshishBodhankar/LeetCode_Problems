class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

def lowestCommonAncestor(p: TreeNode, q: TreeNode):
    """
    Leetcode problem No: 1650
    :param p: Given node 1
    :param q: Given node 2
    :return: Return the least common ancestor of p and q
    """

    ## STEP 1: identify the depth of the two nodes within the tree
    def caliberateDepth(node):
        if not node:
            return 0
        d = 0
        curr = node
        while curr:
            d += 1
            curr = curr.parent
        return d

    d_p, d_q = caliberateDepth(p), caliberateDepth(q)

    ## STEP 2: Move the deeper pointer up until it is at the same level as the other pointer
    curr_p, curr_q = p,q

    if d_p > d_q:
        for _ in range(d_p - d_q):
            curr_p = curr_p.parent
    if d_q > d_p :
        for _ in range(d_q - d_p) :
            curr_q = curr_q.parent

    # PART 3: Move each pointer up level-by-level until they meet
    while curr_p.val != curr_q.val:
        curr_p, curr_q =  curr_p.parent, curr_q.parent

    return curr_p.val

