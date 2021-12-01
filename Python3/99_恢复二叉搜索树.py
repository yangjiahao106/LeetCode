from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(node: TreeNode) -> Tuple:
            if node.left and node.right:
                lMin, lMax = helper(node.left)
                rMin, rMax = helper(node.right)
                if lMin.val > rMin.val:
                    pass


