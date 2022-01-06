from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = root.val

        def dfs(root: TreeNode) -> int:

            l, r = 0, 0
            if root.left:
                l = max(0, dfs(root.left))
            if root.right:
                r = max(0, dfs(root.right))

            self.ans = max(self.ans, root.val + l + r)

            return max(root.val + l, root.val + r)

        dfs(root)
        return self.ans
