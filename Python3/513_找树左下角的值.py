# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 0
        self.res = 0

    def findBottomLeftValue(self, root: TreeNode) -> int:
        """ 深度优先遍历"""
        self.helper(1, root)
        return self.res

    def helper(self, depth, root: TreeNode):
        if root is None:
            return

        if depth > self.max_depth:
            self.max_depth = depth
            self.res = root.val

        self.helper(depth + 1, root.left)
        self.helper(depth + 1, root.right)


from collections import deque


class Solution2:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        """ 广度优先遍历 从右边往左遍历 """
        if root is None:
            return

        q = deque([root])
        q.append(root)
        node = root
        while len(q) > 0:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return node.val
