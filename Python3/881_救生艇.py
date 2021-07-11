from typing import *


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        res = 0
        for i in range(len(people)):
            if people[i] > 0:
                find = False
                for j in range(i + 1, len(people)):
                    if people[j] > 0 and people[i] + people[j] <= limit:
                        find = True
                        res += 1
                        people[i], people[j] = 0, 0  # 标记上船
                        break
                if not find:
                    people[i] = 0
                    res += 1  # 自己上船
        return res


class Solution:
    """
        第一印象应该是会选择两数之和最接近limit的，不会想让最大和最小的一起，
        但是反证下，如果因为它带了最轻的，导致次轻的无法跟其他人同船，
        那么次轻的也一定无法跟最重的乘船。如果次轻的可以跟其他人同船，则反正同船了，跟谁效果都一样。
        所以 不会因为最重的选择了最轻的同船，导致后面的配对结果更坏。
    """

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                l += 1
            res += 1
        return res
