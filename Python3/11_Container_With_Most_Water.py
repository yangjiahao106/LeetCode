#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/8
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        "暴力算法 超时了"
        """
        content = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if ((j - i) * min(height[i], height[j])) > content:
                    content = (j - i) * min(height[i], height[j])
        return content


class Solution2:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        "O(n) 100ms"
        """
        content = 0
        i = 0
        j = len(height) - 1
        while j > i:
            if (j - i) * min(height[i], height[j]) > content:
                content = (j - i) * min(height[i], height[j])
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return content


from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        "O(n) 52ms"

        res = 0
        l = 0
        r = len(height) - 1
        max_height = max(height)

        while l < r:
            # 神来之手
            if res > max_height * (r - l):
                break
            if height[l] < height[r]:
                res = max(res, (r - l) * height[l])
                l += 1
            else:
                res = max(res, (r - l) * height[r])
                r -= 1
        return res


if __name__ == '__main__':
    so = Solution2()
    ret = so.maxArea([1, 1])
    print(ret)
