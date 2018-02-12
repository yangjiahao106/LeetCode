#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/12
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        node = head
        head = head.next
        nodes = []
        for i in range(4):
            if node is not None:
                nodes.append(node)
                node = node.next

        while len(nodes) == 4:
            nodes[1].next = nodes[0]
            nodes[0].next = nodes[3]
            for i in range(2):
                if node is not None:
                    nodes.append(node)
                    node = node.next
            nodes = nodes[2:]

        if len(nodes) == 2:
            nodes[1].next = nodes[0]
            nodes[0].next = None
            return head
        else:
            nodes[1].next = nodes[0]
            nodes[0].next = nodes[2]
            return head


class Solution2:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        p2.next = self.swapPairs(p2.next)
        p1.next = p2.next
        p2.next = p1
        head = p2
        return head



if __name__ == '__main__':
    node = head = ListNode(0)
    for i in range(1,12):
        node.next = ListNode(i)
        node = node.next

    so = Solution2()
    res = so.swapPairs(head)

    while res:
        print(res.val, end=' ')
        res = res.next

