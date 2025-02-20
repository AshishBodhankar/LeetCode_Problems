class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
    """
    Leetcode problem No: 236
    :param root: Root node of a binary tree
    :param p: Given node 1
    :param q: Given node 2
    :return: Return the least common ancestor of p and q with the root node BT
    """

    lca = [root]

    def recur(node,p,q):
        if not node:
            return False

        left = recur(node.left,p,q)
        right = recur(node.right,p,q)


        mid = node.val == p.val or node.val == q.val

        if mid + left + right == 2:
            lca[0] = node

        return mid or left or right

    recur(root,p,q)
    return lca[0]

