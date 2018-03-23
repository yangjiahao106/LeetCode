#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/23

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        p1, p2 = 0, len(rotateArray)-1
        mid = p1

        while p1<p2:
            # if p2-p1 == 1:
            #     return rotateArray[p2]
            mid = (p1+p2)//2

            if rotateArray[mid] == rotateArray[p1] == rotateArray[p2]: # 此时需要遍历
                return min(rotateArray)

            if rotateArray[mid]>=rotateArray[p1]:
                p1= mid
            if rotateArray[mid]<=rotateArray[p2]:
                p2 = mid

        return rotateArray[mid]


if __name__ == '__main__':
    so = Solution()
    res = so.minNumberInRotateArray([1,2,0,1,1,1,1])
    print(res)