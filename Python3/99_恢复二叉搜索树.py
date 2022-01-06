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
        3 2 1
        1 2 3


        1 3 2 4
        """

        self.pre = None
        self.left_node = None

        def in_order_l(root: TreeNode):
            if root is None:
                return
            in_order_l(root.left)
            if self.pre and root.val < self.pre.val:
                self.left_node = self.pre
                return
            self.pre = root
            in_order_l(root.right)

        in_order_l(root)

        self.pre = None

        def in_order_r(root: TreeNode):
            if root is None:
                return
            in_order_r(root.right)

            if self.pre and root.val > self.pre.val:
                self.left_node.val, self.pre.val = self.pre.val, self.left_node.val
                return
            self.pre = root
            in_order_r(root.left)

        in_order_r(root)


class Solution2:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second = None, None

        stack = list()
        cur, pre = root, None

        # 中序遍历
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if pre and cur.val < pre.val:
                if not first:
                    first = pre
                second = cur

            pre = cur
            cur = cur.right

        first.val, second.val = second.val = first.val

        # stk = []
        # while stk or cur:
        #     if cur:
        #         stk.append(cur)
        #         cur = cur.left
        #     else:
        #         cur = stk.pop()
        #         if pre and pre.val > cur.val:
        #             if not first: first = pre
        #             second = cur
        #         pre = cur
        #         cur = cur.right
        #
        # first.val, second.val = second.val, first.val
