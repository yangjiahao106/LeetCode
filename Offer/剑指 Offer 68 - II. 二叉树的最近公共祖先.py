# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1 = []
        self.find_path(root, path1, p)

        path2 = []
        self.find_path(root, path2, q)

        ans = None
        for i in range(min(len(path1), len(path2))):
            if path1[i] != path2[i]:
                break
            ans = path1[i]

        return ans

    def find_path(self, root, path, target):
        if not root:
            return False
        path.append(root)

        if root == target:
            return True

        if self.find_path(root.left, path, target):
            return True
        if self.find_path(root.right, path, target):
            return True
        path.pop()


class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)

        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right
