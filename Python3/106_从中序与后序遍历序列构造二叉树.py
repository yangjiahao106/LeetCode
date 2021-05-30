# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return root
