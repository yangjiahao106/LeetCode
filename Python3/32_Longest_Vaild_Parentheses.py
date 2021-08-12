#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = [-1]  # 栈，后进先出

        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i) # 将（ 放入栈中
            else:
                stack.pop()  # 从栈中取出一个 （
                if len(stack) == 0:  # stack为空时，右括号比左括号多一个，将此右括号作为起始点，再次查找。
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


class Solution2:
    """ 动态规划
    ()(())
    """

    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif dp[i - 1] > 0 and i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':

                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

        return max(dp)


if __name__ == '__main__':
    so = Solution()
    res = so.longestValidParentheses("())()())")
    # ()(()
    print(res)
