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
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        slow, fast = head, head.next
        dul = ' '
        while fast.next:
            if fast.val == dul or fast.val == fast.next.val:
                dul = fast.val
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next

        if fast.val == dul:
            slow.next = None
        else:
            slow.next = fast

        return head.next


class Solution2:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next

        return dummy.next


if __name__ == '__main__':
    so = Solution()

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = so.deleteDuplicates(head)

    while res:
        print(res.val)
        res = res.next
