#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/13

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)


class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = []
        res = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

    def PreOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = []
        res = []
        while node or stack:
            if node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return res

    def PostOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = []
        res = []
        lastVisited = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right and lastVisited != peek.right: # lastVisited 防止重复遍历右节点。
                    node = peek.right
                else:
                    res.append(peek.val)
                    lastVisited = stack.pop()
        return res


# iterativePostorder(node)
#   s ← empty stack
#   lastNodeVisited ← null
#   while (not s.isEmpty() or node ≠ null)
#     if (node ≠ null)
#       s.push(node)
#       node ← node.left
#     else
#       peekNode ← s.peek()
#       // if right child exists and traversing node
#       // from left child, then move right
#       if (peekNode.right ≠ null and lastNodeVisited ≠ peekNode.right)
#         node ← peekNode.right
#       else
#         visit(peekNode)
#         lastNodeVisited ← s.pop()


if __name__ == '__main__':
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.left.left = TreeNode('C')
    root.left.right = TreeNode('D')
    root.left.right.left = TreeNode('E')
    root.left.right.right = TreeNode('F')
    root.left.right.left.left = TreeNode('G')

    so = Solution2()
    res = so.PostOrderTraversal(root)
    print(res)

    so = Solution()
