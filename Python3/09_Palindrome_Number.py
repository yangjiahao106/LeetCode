#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/3
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        rev = 0  # 反转后的数字, 其他语言需要考虑反转后溢出的问题
        while tmp:
            rev = rev * 10 + tmp % 10
            tmp = tmp // 10
        return rev == x

    def isPalindrome2(self, x):
        if x < 0:
            return False
        e = len(str(x))
        for i in range(e // 2):
            if x % 10 != x // 10 ** (e - 1 - i * 2):
                return False
            x = x // 10
            x = x % (10 ** (e - 2 - i * 2))
        return True


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # 只反转一半数字，不会溢出，需要特殊处理 以0结尾的数字

        if x % 10 == 0 and x != 0:
            return False

        rev = 0  # 反转后的数字, 其他语言需要考虑反转后溢出的问题
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        return rev == x or x == rev // 10  # 偶数位则相等， 奇数位则 x == rev//10




if __name__ == '__main__':
    s = Solution()
    i = s.isPalindrome2(123321)
    print(i)
    # 12321
