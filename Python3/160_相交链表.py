# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a and b:
            a = a.next
            b = b.next

        while a:
            headA = headA.next
            a = a.next

        while b:
            headB = headB.next
            b = b.next

        while headA:
            if headA == headB:
                return headA

            headA, headB = headA.next, headB.next

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        a = headA
        b = headB

        while a != b:
            if a:
                a = a.next
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA

        return a
