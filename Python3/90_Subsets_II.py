#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/13
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.result = [[]]
        self.helper([], nums[:])
        return self.result

    def helper(self, last, rest):
        if not rest:
            return
        for i in range(len(rest)):
            if i == 0 or rest[i] != rest[i - 1]:
                cur = last + [rest[i]]
                self.result.append(cur)
                self.helper(cur, rest[i + 1:])

class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        res = [[]]
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res

if __name__ == '__main__':
    so = Solution()
    res = so.subsetsWithDup([])
    print(res)