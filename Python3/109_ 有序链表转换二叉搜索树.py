from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        分治
        时间复杂度 n*log(n) 链表遍历 log(n) 次
        空间复杂度 log(n)   递归栈的深度
        :param head:
        :return:
        '''
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        slow, fast = head, head
        pre = slow
        while fast and fast.next:  # 快慢指针 找到中点 1 > 2 > 3
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None  # 将链表拆成两个链表

        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)  # 递归构造左右指数
        node.right = self.sortedListToBST(slow.next)
        return node


class Solution2:
    def __init__(self):
        self.head = None

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        中序遍历
        时间复杂度 n
        空间复杂度 log(n)   递归栈的深度
        :param head:
        :return:
        '''
        self.head = head
        n = head
        length = 0
        while n:
            length += 1
            n = n.next

        return self.build(0, length - 1)

    def build(self, left, right):

        if left > right:
            return None

        m = (left + right + 1) // 2

        node = TreeNode(self.head.val)

        node.left = self.build(left, m - 1)
        node.val = self.head.val
        self.head = self.head.next
        node.right = self.build(m + 1, right)
        return node


if __name__ == '__main__':
    pass
