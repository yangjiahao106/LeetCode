from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        l, r = 0, len(nodes) - 1

        """
        偶数个时, 结束条件为 l == r-1, 此时2.next == 3, 只需将3.next 设为None
        1, 2, 3, 4
        
        奇数个时, 结束条件为 l == r, 只需将3.next 设为None
        1，2，3，4，5
        """
        while l < r - 1:
            nodes[l].next = nodes[r]
            nodes[r].next = nodes[l + 1]
            l += 1
            r -= 1

        nodes[r].next = None
        return head


class Solution2:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        找到链表中点将链表分成两部分，将后半部分反转，然后合并两个链表
        """
        # find middle

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        # reverse
        pre = None
        while middle:
            next = middle.next
            middle.next = pre
            pre = middle
            middle = next


        # merge
        head2 = pre
        head1 = head

        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1
            head1 = next1
            head2 = next2

        return head


