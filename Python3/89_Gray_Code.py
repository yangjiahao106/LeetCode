#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/13
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            res.extend([x | 1 << i for x in res[::-1]])
        return res


class Solution2:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1 << n):
            res.append(i ^ i >> 1)
        return res


if __name__ == '__main__':
    so = Solution2()
    res = so.grayCode(4)
    print(res)
