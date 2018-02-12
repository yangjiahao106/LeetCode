#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/12

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swap(self, head, k):
        node = head
        nodes = []
        for i in range(k):
            if node is not None:
                nodes.append(node)
                node = node.next
        nodes.reverse()
        if len(nodes) < k:
            return head

        for i, n in enumerate(nodes[:-1]):
            n.next = nodes[i + 1]

        if node is not None:
            nodes[-1].next = self.swap(node, k)
        else:
            nodes[-1].next = None

        head = nodes[0]
        return head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or head is None:
            return head
        return self.swap(head, k)


if __name__ == '__main__':
    node = head = ListNode(0)
    for i in range(1, 32):
        node.next = ListNode(i)
        node = node.next

    so = Solution()
    res = so.reverseKGroup(head, 5)

    while res:
        print(res.val, end=' ')
        res = res.next
