#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/27
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return 0
        lis = [i for i in range(1, n + 1)]
        for i in range(k - 1):
            self.next(lis, n)

        return ''.join(map(str, lis))

    def next(self, lis, n):
        for i in range(n - 2, -1, -1):
            if lis[i] < lis[i + 1]:
                for j in range(n - 1, -1, -1):
                    if lis[j] > lis[i]:
                        lis[i], lis[j] = lis[j], lis[i]
                        lis[i + 1:] = sorted(lis[i + 1:])
                        return lis


class Solution2:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        rest = [i for i in range(1, n + 1)]
        self.helper(rest, k, res)
        return ''.join(map(str, res))

    def helper(self, rest, k, result):
        if not rest:
            return
        one_group = self.factoral(len(rest) - 1)
        i = (k - 1) // one_group
        result.append(rest[i])
        rest.pop(i)
        return self.helper(rest, k - one_group * i, result)

    def factoral(self, num):
        res = 1
        for i in range(1, num + 1):
            res = res * i
        return res


class Solution3(object):
    def getPermutation(self, n, k):
        nums = [i for i in range(1, 10)]
        k -= 1
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        res = []
        for i in range(n):
            index = k // factorial[n - 1 - i]
            res.append(nums[index])
            nums.remove(nums[index])
            k = k % factorial[n - 1 - i]
        return ''.join(map(str, res))


if __name__ == '__main__':
    so = Solution2()

    res = so.getPermutation(4, 24)
    print(res)
