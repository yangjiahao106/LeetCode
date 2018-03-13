#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/6

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        使用一条链表
        """
        dumpy = ListNode(0)
        dumpy.next = head
        l = r = dumpy
        while r and r.next and r.next.val < x:  # 指针走到第一个 大于x 的前一个节点
            r = r.next
            l = l.next
        while r and r.next:
            if r.next.val < x:
                temp = l.next  # 保存第一个断点的尾部
                temp2 = r.next.next  # 保存第二个断点的尾部
                l.next = r.next
                l = l.next
                l.next = temp
                r.next = temp2
            else:
                r = r.next
        return dumpy.next


class Solution2:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        使用两条链表
        """
        hd1 = p1 = ListNode(0)
        hd2 = p2 = ListNode(0)
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = hd2.next
        return hd1.next


if __name__ == '__main__':
    vals = [4, 2, 3, 1]
    head = node = ListNode(vals[0])
    for val in vals[1:]:
        node.next = ListNode(val)
        node = node.next
    so = Solution()
    res = so.partition(head, 3)

    while res:
        print(res.val, end=' ')
        res = res.next
