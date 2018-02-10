#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/10

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        node = head

        while node != None:
            nodes.append(node)
            node = node.next

        if n == len(nodes):
            head = head.next
            return head
        elif n == 1:
            nodes[-2].next = None
            return head
        else:
            nodes[-(n + 1)].next = nodes[-(n - 1)]
            return head


class Solution2:
    def removeNthFromEnd(self, head, n):
        count, node = 0, head
        while node != None:
            node = node.next
            count += 1

        if n == count:
            return head.next

        i = count - n
        count, node = 0, head
        while node != None:
            count += 1
            if count == i:
                node.next = node.next.next
                return head
            node = node.next


class Solution3(object):
    def removeNthFromEnd(self, head, n):
        first = second = head
        for i in range(n):
            first = first.next

        if first:
            while first.next != None:
                first = first.next
                second = second.next
        else:
            return head.next

        second.next = second.next.next
        return head

if __name__ == '__main__':
    lis = ListNode(1)
    lis.next = ListNode(2)
    lis.next.next = ListNode(3)

    so = Solution3()
    head = so.removeNthFromEnd(lis, 2)
    while head != None:
        print(head.val)
        head = head.next
        # 1 2 3 4 5
