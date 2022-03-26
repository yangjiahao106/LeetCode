# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        def dfs(root: TreeNode):
            if not root:
                return

            dfs(root.left)

            if self.count > k:
                return

            self.count += 1
            if self.count == k:
                self.ans = root.val
                return

            dfs(root.right)

        self.count = 0
        self.ans = 0

        dfs(root)
        return self.ans
