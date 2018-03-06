#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/5
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        left = right = head

        while right.next:
            if right.val == right.next.val:
                right = right.next
            else:
                left.next = right.next
                left = left.next
                right = right.next

        left.next = None
        return head


class Solution2:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next: # while 中 cur 用来排除head为空。
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
