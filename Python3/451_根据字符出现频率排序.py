import collections
class Solution:

    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        l = []
        for k, v in counter.items():
            l.append((v,k))
        l.sort(reverse=True)
        res = ""
        for count, char in l:
            res += char * count
        return res
