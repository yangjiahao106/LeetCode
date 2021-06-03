# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        slow = fast = head
        length = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length += 1
            if slow == fast:
                break

        if slow == fast:
            slow = fast = head
            for i in range(length):
                fast = fast.next
            while True:
                if fast == slow:
                    return slow
                fast = fast.next
                slow = slow.next
        return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow
