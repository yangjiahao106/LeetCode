class Solution:

    def countDigitOne(self, n: int) -> int:
        high = n // 10
        low = 0
        digit = 1
        cur = n % 10

        ans = 0

        while high > 0 or cur > 0:
            if cur == 0:
                ans += high * digit
            elif cur == 1:
                ans += (high * digit) + low + 1
            else:
                ans += (high + 1) * digit

            low += cur * digit

            digit *= 10

            cur = high % 10
            high = high // 10

        return ans


if __name__ == '__main__':
    ans = Solution().countDigitOne(1232)
    print(ans)
