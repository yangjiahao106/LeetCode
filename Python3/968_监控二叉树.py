# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            """
            每个节点分为三种状态 a:有监控， b:能被监控到， c:可以没被监控到
            """
            if root is None:
                # 如果其某个孩子为空，则不能通过在该孩子处放置摄像头的方式，监控到当前节点。因此，该孩子对应的变量 a 应当返回一个大整数，用于标识不可能的情形。

                return [float('inf'), 0, 0]

            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)

            # 后续遍历 从下往上递推
            a = 1 + lc + rc  # 节点有监控
            b = min(a, la + rb, ra + lb)  # 节点能被监控
            c = min(a, lb + rb)  # 节点能不被监控

            return [a, b, c]

        dp = dfs(root)

        return dp[1]
