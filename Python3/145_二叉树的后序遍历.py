from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ 递归 """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, res):
            if root is None:
                return
            helper(root.left, res)
            helper(root.right, res)
            res.append(root.val)

        res = []
        helper(root, res)
        return res


class Solution2:
    """
    栈
    先按照 "中-右-左" 遍历，反转后即为后序遍历 "左-右-中"
    """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left

        return res[::-1]


class Solution3:
    """
    迭代版
    """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        prev = None
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.right is None or root.right == prev:  # 没有右节点或从右节点回来后弹出时才需要输出
                res.append(root.val)
                prev = root
                root = None

            else:
                stack.append(root)  #
                root = root.right
