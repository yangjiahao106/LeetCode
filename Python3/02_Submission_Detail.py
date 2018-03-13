#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/10
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = val2 = 0
        digit = 1
        while l1 or l2:
            if l1:
                val1 += digit * l1.val
                l1 = l1.next
            if l2:
                val2 += digit * l2.val
                l2 = l2.next
            digit *= 10

        val = val1 + val2
        root = ListNode(val % 10)
        val = val // 10
        cursor = root
        while val > 0:
            cursor.next = ListNode(val % 10)
            val = val // 10
            cursor = cursor.next
        return root