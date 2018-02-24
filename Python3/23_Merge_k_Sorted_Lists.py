#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/11
# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    递归 两两合并
    错误：内存溢出
    时间复杂度：O(m^n)
    """

    def merge(self, lists):
        if len(lists) == 1:
            return lists[0]
        if lists[0] == None:
            return self.merge(lists[1:])
        if lists[1] == None:
            return self.merge(lists[:1] + lists[2:])
        l1, l2 = lists[0], lists[1]
        node = head = ListNode(0)
        while l1 and l2:
            if l2.val <= l1.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        node.next = l1 if l1 else l2
        lists.append(head.next)
        return self.merge(lists[2:])

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.merge(lists)


class Solution1_1:
    """
    分治算法
    runtime:600ms
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        def merge(l1, l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1

            node = head = ListNode(0)
            while l1 and l2:
                if l2.val <= l1.val:
                    node.next = l2
                    l2 = l2.next
                else:
                    node.next = l1
                    l1 = l1.next
                node = node.next
            node.next = l1 if l1 else l2
            return head.next

        while len(lists) > 1:
            ret = merge(lists[0], lists[1])
            lists = lists[2:]
            lists.append(ret)
        return lists[0]


import queue


class Solution2:
    """
    优先队列
    时间负责度：O(m * n * log n)
    runtime: 250ms
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        node = head = ListNode(0)
        pq = queue.PriorityQueue()
        for i, li in enumerate(lists):
            if li is not None:
                pq.put([li.val, i])

        while not pq.empty():
            _, index = pq.get()
            node.next = lists[index]
            node = node.next
            if lists[index].next == None:
                pass
            else:
                lists[index] = lists[index].next
                pq.put([lists[index].val, index])

        return head.next


class Solution3:
    """
    获取所有节点的val，排序后重新建立列表
    时间负责度 O(m*n)
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums = []
        for li in lists:
            while li is not None:
                nums.append(li.val)
                li = li.next

        if len(nums) == 0:
            return None

        nums.sort()
        head = node = ListNode(nums[0])
        for i in nums[1:]:
            node.next = ListNode(i)
            node = node.next
        return head


import heapq


class Solution4:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res_head, res_tail = None, None

        def value_item_pair(item, uid):
            return (item.val, uid, item)

        uid = 0  # for stable sorting in heapq
        h = []
        for item in filter(lambda lst: lst, lists):
            heapq.heappush(h, value_item_pair(item, uid))
            uid += 1

        while h:
            val, uid, item = heapq.heappop(h)

            node = ListNode(val)
            if res_head is None:
                res_head = node
            if res_tail:
                res_tail.next = node
            res_tail = node

            if item.next:
                heapq.heappush(h, value_item_pair(item.next, uid))

        return res_head


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)
    l3 = ListNode(5)
    l3.next = ListNode(8)
    l3.next.next = ListNode(9)

    so = Solution3()
    ret = so.mergeKLists([l1, None, l2, l3])
    print("return: ", ret)

    while ret:
        print(ret.val, end=' ')
        ret = ret.next
