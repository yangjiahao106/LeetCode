class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        ans = [0] * len(a)
        left_sum = 1
        for k, v in enumerate(a):
            ans[k] = left_sum
            left_sum *= v

        right_sum = 1
        for i in range(len(a) - 1, -1, -1):
            ans[i] = ans[i] * right_sum
            right_sum *= a[i]

        return ans
