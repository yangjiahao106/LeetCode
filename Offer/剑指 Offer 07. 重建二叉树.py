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
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])  # 注意 preorder[idx+1:]
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build(root, left, right):
            if left > right:
                return None

            node = TreeNode(preorder[root])
            i = index[preorder[root]]

            node.left = build(root + 1, left, i - 1)
            node.right = build(root + (i - left + 1), i + 1, right)
            return node

        index = dict()
        for i in range(len(inorder)):
            index[inorder[i]] = i

        return build(0, 0, len(preorder) - 1)


if __name__ == '__main__':
    Solution().buildTree([1, 2, 3], [2, 3, 1])
