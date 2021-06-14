# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""BFS"""


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        res = []
        q = [root]
        while q:
            n: TreeNode = q.pop(0)
            if n is not None:
                res.append(str(n.val))
                q.append(n.left)
                q.append(n.right)
            else:
                res.append("X")

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        vals = data.split(",")
        root = TreeNode(int(vals.pop(0)))
        nodes = [root]

        while vals:
            left = vals.pop(0)
            right = vals.pop(0)
            node = nodes.pop(0)

            if left != "X":
                leftNode = TreeNode(int(left))
                nodes.append(leftNode)
                node.left = leftNode

            if right != "X":
                rightNode = TreeNode(int(right))
                nodes.append(rightNode)
                node.right = rightNode

        return root


"""DFS"""


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "X"

        return root.val + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        return self.helper(vals)

    def helper(self, vals: list):

        v = vals.pop(0)
        if v == "X":
            return None
        node = TreeNode(int(v))
        node.left = self.helper(vals)
        node.right = self.helper(vals)
