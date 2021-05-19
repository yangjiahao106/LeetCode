

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        for i, v1 in enumerate(nums):
            maxv, idx = "0", -1
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i] and nums[j] > maxv:
                    maxv = nums[j]
                    idx = j
            if idx >= 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
        return int("".join(nums))



if __name__ == '__main__':
    print(Solution().maximumSwap(2736))
