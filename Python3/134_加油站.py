from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """暴力解法 n*n"""
        for j in range(len(gas)):
            i = j
            count = 0
            while True:
                if gas[i] + count >= cost[i]:
                    count += gas[i] - cost[i]
                    i += 1
                    if i == len(gas):
                        i = 0
                    if i == j:
                        return j
                else:
                    break
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_rest = 0
        rest = 0
        start = 0
        for i in range(len(gas)):
            total_rest += (gas[i] - cost[i])
            rest += (gas[i] - cost[i])
            if rest < 0:
                rest = 0
                start = i + 1

        if total_rest < 0:
            return -1
        return start


class Solution3:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start
