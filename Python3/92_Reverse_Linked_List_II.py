#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/13
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dumpy = ListNode(0)
        dumpy.next = head

        start = dumpy
        for _ in range(m - 1):
            start = start.next

        pre = end = start.next
        cur = pre.next

        for _ in range(n - m):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        start.next = pre
        end.next = cur
        return dumpy.next



if __name__ == '__main__':
    head = node = ListNode(0)
    vals = [1,2,3,4,5]
    for val in vals:
        node.next = ListNode(val)
        node = node.next

    so = Solution()
    res = so.reverseBetween(head.next,1,5)
    while res:
        print(res.val,end=' ')
        res = res.next