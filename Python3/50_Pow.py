#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/23
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n


class Solution2:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x, n - 1)


class Solution3:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n & 1:  # 如果为奇数 n % 2 == 1
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    so = Solution()
    res = so.myPow(1.1, 2)
    print(res)
