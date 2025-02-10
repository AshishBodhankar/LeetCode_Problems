# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(root):
    def same(node1, node2) :
        if not node1 and not node2 :
            return True
        elif not node1 or not node2 :
            return False
        elif node1.val != node2.val :
            return False
        else :
            return same(node1.left, node2.right) and same(node1.right, node2.left)

    return same(root, root)