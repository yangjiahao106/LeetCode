class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1

        if 25 >= num % 100 >= 10:
            return self.translateNum(num // 10) + self.translateNum(num // 100)

        return self.translateNum(num // 10)
