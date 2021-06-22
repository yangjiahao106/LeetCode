"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
        使用字典保存节点对应关系
        时间复杂度O(n)
        空间复杂度O(n)
    """

    def copyRandomList(self, head: 'Node') -> 'Node':
        d = dict()

        cur = head

        while cur:
            newNode = Node(cur.val)
            d[cur] = newNode
            cur = cur.next
        cur = head

        while cur:
            d[cur].random = d[cur.random] if cur.random else None
            d[cur].next = d[cur.next] if cur.random else None
            cur = cur.next

        return d[head]


class Solution2:
    """
        记忆化递归
        时间复杂度O(n)
        空间复杂度O(n)
    """

    def __init__(self):
        self.bp = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        if head in self.bp:
            return self.bp[head]

        newNode = Node(head.val)
        self.bp[head] = newNode
        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)
        return newNode


class Solution3:
    """
        克隆节点放到原节点后面
        时间复杂度O(n)
        空间复杂度O(1)
        // 1->2->3  ==>  1->1'->2->2'->3->3'

    """

    def copyRandomList(self, head: 'Node') -> 'Node':
        pass




if __name__ == '__main__':
    n = Node(2)
    d = {n: 1}

    print(d[n])
