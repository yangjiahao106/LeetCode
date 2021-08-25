from typing import *


class Solution:
    """
    单调栈 44ms defeat 66%

    """

    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []  # stack 是单调递减的

        for r in range(len(height)):

            while stack and height[stack[-1]] < height[r]:
                top = stack.pop()
                if not stack:
                    break  # 没有左边界，无法存住水，直接break

                l = stack[-1]  # l 为左边界
                width = r - l - 1
                height_ = min(height[l], height[r]) - height[top]
                res += width * height_

            stack.append(r)

        return res


class Solution:
    """
    双指针法 44ms defeat 66%
    维护一个 leftMax 和 rightMax
    """

    def trap(self, height: List[int]) -> int:
        l_max, r_max = 0, 0
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)

            if height[l] < height[r]:
                res += (min(l_max, r_max) - height[l])
                l += 1
            else:
                res += (min(l_max, r_max) - height[r])
                r += 1
        return res


if __name__ == '__main__':
    res = Solution().trap([4, 2, 0, 3, 2, 5])
    print(res)
