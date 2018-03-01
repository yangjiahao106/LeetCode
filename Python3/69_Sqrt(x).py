#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/1
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return (int(x ** 0.5))


class Solution2:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        数学算法
        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


class Solution3:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        二分查找
        """
        if x == 0:
            return 0
        low, high = 1, x
        while True:
            mid = (low + high) // 2
            if mid > x / mid:
                high = mid - 1
            else:
                if mid + 1 >= x / (mid + 1):  # 如果 mid 小了或正好，mid + 1 大了
                    return mid
                low = mid + 1


if __name__ == '__main__':
    so = Solution()
    res = so.mySqrt(1)
    print(res)
