#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/19
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        时间复杂度O(n*n)
        """
        nums = [x for x in range(max(height), -1, -1)]
        full_capacity = 0
        for j in range(len(nums)):
            capacity, prev = 0, -1
            for i, h in enumerate(height):
                if h in nums[:j + 1]:
                    if prev != -1:
                        capacity += (i - prev - 1)
                    prev = i
            full_capacity += capacity
        return full_capacity


class Solution2:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        时间复杂度 O(n)
        """
        left = full_capacity = capacity = 0
        for right in range(1, len(height)):
            if height[right] >= height[left]:
                capacity = (right - left - 1) * min(height[right], height[left])
                for box in height[left+1:right]:
                    capacity -= box
                left = right
                full_capacity += capacity

        end, right = left, len(height)-1
        for left in range(len(height)-1, end-1,-1):
            if height[left] > height[right]:
                capacity = (right - left - 1) * min(height[right], height[left])
                for box in height[left+1:right]:
                    capacity -= box
                right = left
                full_capacity += capacity
        return full_capacity

class Solution3:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        时间复杂度 O(n)

        """
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        result = 0
        while left<right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    result += left_max-height[left]
                left_max = max(left_max,height[left])
                left+=1
            else:
                if height[right] < right_max:
                    result += right_max-height[right]
                right_max = max(right_max,height[right])
                right-=1
        return result

if __name__ == '__main__':
    so = Solution2()
    res = so.trap([1,1,2])
    print(res)
