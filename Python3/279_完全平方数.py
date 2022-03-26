class Solution:
    """
    背包，动态规划
    """

    def numSquares(self, n: int) -> int:

        dp = [1000] * (n + 1)

        dp[0] = 0
        for i in range(1, n + 1):
            if i * i > n:
                break
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)

        return dp[-1]


import math


class Solution:
    def numSquares(self, n: int) -> int:
        # 贪心，依次实验是由1个完全平方数组成？2个？3个？...直到试出结果来
        # 首先用集合存放不大于n的完全平方数，便于后面查找
        ns = set([i * i for i in range(1, int(math.sqrt(n)) + 1)])

        # 判断n是否由count个数字组成
        def divisible(n, count):
            # 查看自己是否是完全平方数
            if count == 1:
                return n in ns
            for num in ns:
                # 减去一个完全平方数，看看是否满足
                if n - num > 0:
                    if divisible(n - num, count - 1):
                        return True
            return False

        # 最多是由n个1构成
        for count in range(1, n + 1):
            if divisible(n, count):
                return count


from collections import deque


class Solution:
    """DFS  """

    def numSquares(self, n: int) -> int:

        deq = deque()
        deq.append(n)
        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]

        visited = set()
        step = 0
        while deq:
            step += 1

            for i in range(len(deq)):
                number = deq.popleft()
                for s in squares:
                    target = number - s
                    if target < 0:
                        break
                    if target == 0:
                        return step
                    if target not in visited:
                        deq.append(target)
                        visited.add(target)
        return 0

