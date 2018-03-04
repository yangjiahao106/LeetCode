#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/3
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        dp = [[i] for i in range(1, n + 1)]
        for _ in range(k - 1):
            temp = []
            for each in dp:
                for nex in range(each[-1] + 1, n + 1):
                    temp.append(each + [nex])
            dp = temp
        return dp


class Solution2:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1


class Solution3:
    def combine(self, n, k):
        result = [[]]
        for _ in range(k):
            result = [[i] + c for c in result for i in range(1, c[0] if c else n + 1)]
        return result


if __name__ == '__main__':
    so = Solution2()
    res = so.combine(4, 3)
    print(res)
