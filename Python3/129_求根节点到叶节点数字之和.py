# Definition for a binary tree node.

from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """深度优先遍历"""

    def sumNumbers(self, root: TreeNode) -> int:
        return self.helper(0, root)

    def helper(self, v, root) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return v * 10 + root.val

        return self.helper(v * 10 + root.val, root.left) + self.helper(v * 10 + root.val, root.right)


class Solution2:
    """广度优先遍历"""

    def sumNumbers(self, root: TreeNode) -> int:
        nodeQ = Queue()
        sumQ = Queue()

        nodeQ.put(root)
        sumQ.put(0)
        res = 0
        while not nodeQ.empty():
            node = nodeQ.get()
            sum = sumQ.get()

            if node.left is None and node.right is None:
                res += (sum * 10 + node.val)

            if node.left:
                nodeQ.put(node.left)
                sumQ.put(sum * 10 + node.val)

            if node.right:
                nodeQ.put(node.right)
                sumQ.put(sum * 10 + node.val)
        return res


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    print(Solution2().sumNumbers(root))
