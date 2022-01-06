# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # 深度遍历 不断缩小边界
        def dfs(root: TreeNode, min_, max_) -> bool:
            if root is None:
                return True

            if root.val >= max_ or root.val <= min_:
                return False

            return dfs(root.left, min_, min(root.val, max_)) and dfs(root.right, max(root.val, min_), max_)

        return dfs(root, float('-inf'), float('inf'))


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        # 利用 二叉搜索树 "中序遍历有序" 的特性

        self.pre = float("-inf")

        def dfs(root) -> bool:
            if root is None:
                return True
            if not dfs(root.left):
                return False
            if root.val <= self.pre:
                return False

            self.pre = root.val

            return dfs(root.right)

        return dfs(root)
