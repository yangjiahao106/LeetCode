#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/10

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif len(stack) == 0 or c != stack.pop():
                return False

        return len(stack) == 0


class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True

        if n % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')

        return s == ''


if __name__ == '__main__':
    so = Solution()
    s = "({()[]}{})"
    ret = so.isValid(s)
    print(ret)
