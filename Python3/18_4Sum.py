class Solution:
    # time complexity n^3
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while r > l:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while r > l and nums[l] == nums[l+1]:
                            l += 1
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res

class Solution2():
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return
if __name__ == '__main__':
    so = Solution()
    ret = so.fourSum([-3,-2,-1,0,0,1,2,3], 0)
    print(ret)
