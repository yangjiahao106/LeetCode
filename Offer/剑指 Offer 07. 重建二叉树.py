# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])  # 注意 preorder[idx + 1:]
        root.right = self.buildTree(preorder[idx:], inorder[idx + 1:])  # 注意 preorder[idx:]
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(l, r):
            pass
