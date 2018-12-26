#! python3
# __author__ = "YangJiaHao"
# date: 2018/12/25














def duplicate(nums):
    length = len(nums)

    for n in nums:
        if n < 0 or n >= length:
            return False

    for i in range(len(nums)):

        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

    return False
