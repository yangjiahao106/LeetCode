class Solution:
    def sumNums(self, n: int) -> int:
        # return sum(range(1,n+1))
        if n <= 1: return n
        return n + self.sumNums(n - 1)
