#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/11
import copy


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = list(n * '(')
        right = list(n * ')')
        res = []

        def generator(one, left, right):
            if len(left) == 0:
                res.append(one + ''.join(right))
                return 0

            if len(left) < len(right):
                generator(one + left[-1], left[:-1], right[:])
                generator(one + right[-1], left[:], right[:-1])

            if len(right) == len(left):
                generator(one + left[-1], left[:-1], right[:])

        generator('', left[:], right[:])

        return res

class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = right = n
        res = []

        def generator(one, left, right):
            if left == 0:
                res.append(one + ')'*right)
                return 0

            if left < right:
                generator(one + '(', left - 1, right)
                generator(one + ')', left, right - 1)

            if right == left:
                generator(one + '(', left -1, right)

        generator('', left, right)
        return res


class Solution3(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]


if __name__ == '__main__':
    so = Solution2()
    ret = so.generateParenthesis(2)
    print(ret)
