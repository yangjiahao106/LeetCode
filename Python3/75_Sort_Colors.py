#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/2
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        two point
        时间复杂度O(3n)
        """
        slow = 0
        start = 0 # fast指针起始位置
        for color in range(3):
            for fast in range(start, len(nums)):
                if nums[fast] == color:  # 颜色
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
            start = slow

        # print(nums)

    class Solution:
        def sortColors(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            时间复杂度O(n)
            """
            l, m, r = 0, 0, len(nums) - 1

            while m <= r:

                if nums[m] == 0:
                    nums[l], nums[m] = nums[m], nums[l]
                    m += 1
                    l += 1
                elif nums[m] == 1:
                    m += 1
                else:
                    nums[m], nums[r] = nums[r], nums[m]
                    r -= 1

# class Solution {
# public:
#     void sortColors(int A[], int n) {
#         int i = 0, j = n-1;
#         for(int k=0; k<=j; )
#         {
#         	if(A[k]==0)  swap(A[i++], A[k++]);
#         	else if(A[k]==2)  swap(A[j--], A[k]);
#         	else k++;
#         }
#     }
# };

if __name__ == '__main__':
    so = Solution()
    res = so.sortColors([0, 1,2,0,1, 2, 1,2, 1, 0])
