#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        stack = [-1]  # 栈，后进先出

        for i in range(start, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()  # 出最后一个数据
                if (len(stack) == 0):  # stack为空时，右括号比左括号多一个，将此右括号作为起始点，再次查找。
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


if __name__ == '__main__':
    so = Solution()
    res = so.longestValidParentheses("())()())")
    # ()(()
    print(res)
