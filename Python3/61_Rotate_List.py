#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/28
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0:
            return head

        point, length = head, 1
        while point.next:
            point = point.next
            length += 1

        leftPoint = rightPoint = head
        for i in range(k % length):  # 如果k==length 为0
            rightPoint = rightPoint.next

        while rightPoint.next:
            rightPoint = rightPoint.next
            leftPoint = leftPoint.next

        rightPoint.next = head
        head = leftPoint.next
        leftPoint.next = None

        return head


class Solution2:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        storeList = []
        current = head
        while current != None:
            storeList.append(current)
            current = current.next
        if len(storeList) <= 1:
            return head
        k = k % len(storeList)
        if k == 0:
            return head
        res = storeList[-k]
        storeList[-k - 1].next = None
        storeList[-1].next = head
        return res
