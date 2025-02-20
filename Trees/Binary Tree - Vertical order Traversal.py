# Definition for a binary tree node.
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: TreeNode) -> list:

    if not root:
        return []

    result = defaultdict(list)
    queue = deque()
    queue.append((root,0))

    while queue:
        node,index = queue.popleft()
        result[index].append(node.val)

        if node.left:
            queue.append((node.left, index-1))
        if node.right:
            queue.append((node.right,index+1))

    return [result[key] for key in sorted(result.keys())]

