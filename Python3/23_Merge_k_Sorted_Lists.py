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
    分治算法, 参考归并排序
    runtime:76ms
    """

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None

        def merge(list1, list2):
            if len(list1) > 1:
                m = len(list1) // 2
                list1 = merge(list1[:m], list1[m:])

            if len(list2) > 1:
                m = len(list2) // 2
                list2 = merge(list2[:m], list2[m:])

            if not list1:
                return list2
            if not list2:
                return list1

            l, r = list1[0], list2[0]
            head = cur = ListNode(0)
            while l and r:
                if l.val <= r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            if l:
                cur.next = l
            if r:
                cur.next = r

            return [head.next]

        return merge([], lists)[0]


class Solution2:
    """
    分治算法, 简洁版
    """

    def mergeKLists(self, lists):
        if not lists: return None

        def merge(l, r):
            head = cur = ListNode(0)
            while l and r:
                if l.val <= r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            cur.next = l if l else r
            return head.next

        def divide(l, r):
            if l == r:  # 区间内只有一个时直接返回 ， 否则继续分隔
                return lists[l]
            mid = (l + r) // 2
            left = divide(l, mid)
            right = divide(mid + 1, r)  # [] 左闭右闭， 所以左边是 mid+1
            return merge(left, right)

        return divide(0, len(lists) - 1)


class Solution3:
    """
    使用优先队列
    时间负责度：O(m * n * log n)
    runtime: 52 ms
    """

    def mergeKLists(self, lists):
        import heapq
        res_head = cur = ListNode(0)
        h = []
        for idx, node in enumerate(lists):
            if node:
                # (node.val, node) 当val 重复时 node 不可比较会报错，所以使用 idx。 也可以插入一个自增值比如 (node.val, i, node)
                heapq.heappush(h, (node.val, idx))

        while h:
            val, idx = heapq.heappop(h)
            cur.next = lists[idx]
            cur = lists[idx]
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(h, (lists[idx].val, idx))
        return res_head.next


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

    so = Solution2()
    ret = so.mergeKLists([l1, None, l2, l3])
    print("return: ", ret)

    while ret:
        print(ret.val, end=' ')
        ret = ret.next
