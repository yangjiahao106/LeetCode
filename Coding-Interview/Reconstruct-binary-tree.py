#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/17

# -*- coding:utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        root = TreeNode(pre[0])
        mid = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:mid + 1], tin[:mid])
        root.right = self.reConstructBinaryTree(pre[mid + 1:], tin[mid + 1:])
        return root

if __name__ == '__main__':
    so = Solution()
    res = so.reConstructBinaryTree(list('12473568'),list('47215386'))
