# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 找到中点
        if head is None or head.next is None:
            return head

        slow, fast = head, head
        pre = slow
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        # 合并
        return self.merge(left, right)


    def merge(self, left, right):
        new_head = ListNode(-1)
        p = new_head
        while left and right:
            if left.val <= right.val:
                p.next = left
                p = p.next
                left = left.next
            else:
                p.next = right
                p = p.next
                right = right.next

        if left:
            p.next = left

        if right:
            p.next = right

        return new_head.next
