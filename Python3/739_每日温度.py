from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                l = stack.pop()
                res[l] = i - l
            stack.append(i)
        return res



if __name__ == '__main__':
    res = Solution().dailyTemperatures([1,4,2,9,10])
    print(res )