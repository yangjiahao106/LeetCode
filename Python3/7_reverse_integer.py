#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/3

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        symbol = 1
        y = 0
        if x < 0:
            x = -x
            symbol = -1
         
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10
        y *= symbol

        if y < -2147483648 or y > 2147483647:
            return 0
        return y

    def reverse2(self, x):
        y = int(str(abs(x))[::-1])
        if y < -2147483648 or y > 2147483647 or y == 0:
            return 0
        if x >= 0:
            return y
        if x < 0:
            return -y


if __name__ == '__main__':
    so = Solution()
    y = so.reverse2(-24)
    print(y)
