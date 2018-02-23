#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/22

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #基于permutations 1 使用set进行去重。
        """
        dp = {()}
        for num in nums:
            temp = set()
            for li in dp:
                for pos in range(len(li) + 1):
                    temp.add(li[:pos] + (num,) + li[pos:])
            dp = temp
        return list(dp)


class Solution2:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        all_result = []
        nums.sort()
        self.helper([], nums, all_result)
        return all_result

    def helper(self, result, rest, all_results):
        if rest == []:
            return all_results.append(result)
        for i, v in enumerate(rest):
            if i > 0 and rest[i] == rest[i - 1]:  # 去重
                continue
            self.helper(result + [v], rest[:i] + rest[i + 1:], all_results)  #


class Solution3:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break  # 使用break 而不是continue可以去除 2112 2112的重复
            ans = new_ans
        return ans


if __name__ == '__main__':
    so = Solution2()
    res = so.permuteUnique([1, 2, 2, 1])
    print(res)
