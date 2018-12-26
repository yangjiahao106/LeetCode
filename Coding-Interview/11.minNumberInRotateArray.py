#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/23

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        p1, p2 = 0, len(rotateArray) - 1
        mid = 0

        while rotateArray[p1] >= rotateArray[p2]:
            if p2-p1 == 1:
                return rotateArray[p2]

            mid = (p1 + p2) // 2

            if rotateArray[mid] == rotateArray[p1] == rotateArray[p2]:  # 此时需要遍历
                return min(rotateArray)

            if rotateArray[mid] >= rotateArray[p1]:
                p1 = mid
            if rotateArray[mid] <= rotateArray[p2]:
                p2 = mid

        return rotateArray[mid]


def my_solution(array):

    if not array:
        return 0

    p1, p2 = 0, len(array) - 1
    mid = 0

    while array[p1] >= array[p2]:
        if p2 - p1 <= 1:
            return array[p2]

        mid = (p2 - p1) // 2

        if array[p1] == array[mid] == array[p2]:

            return min(array[p1:p2])

        if array[mid] >= array[p2]:
            p1 = mid

        elif array[mid] <= array[p1]:
            p2 = mid


if __name__ == '__main__':
    so = Solution()
    res = so.minNumberInRotateArray([1, 2, 0, 1, 1, 1, 1])
    print(res)
