from typing import *


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        import collections
        cs = sorted(collections.Counter(questions).values(), reverse=True)
        c = 0
        for i, v in enumerate(cs):
            c += v
            if c >= len(questions) // 2:
                return i + 1
