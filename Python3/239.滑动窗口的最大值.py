from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = []
        ans = []
        for i in range(k):
            while len(que) > 0 and nums[i] > que[-1][0]:
                que.pop()
            que.append((nums[i], i))
        ans.append(que[0][0])

        for i in range(k, len(nums)):
            n = nums[i]
            while len(que) > 0 and n > que[-1][0]:
                que.pop()
            que.append((n, i))

            while que[0][1] <= i - k:
                que.pop(0)
            ans.append(que[0][0])

        return ans


class Slution2:
    # 单调队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        ans = []
        for i in range(k):
            while len(q) > 0 and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)
        ans.append(nums[q[0]])

        for i in range(k, len(nums)):
            while len(q) > 0 and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


if __name__ == '__main__':
    pass
