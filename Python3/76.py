#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/3

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = dict()
        for a in t:
            if a not in m:
                m[a] = -1
            else:
                m[a] -= 1

        ok_len = 0
        l = 0
        left, right = 0, len(s) - 1
        length = len(s)

        for r, c in enumerate(s):
            if c in m:
                m[c] += 1
                if m[c] == 0:
                    ok_len += 1

            if ok_len == len(m):
                while s[l] not in m or m[s[l]] > 0:
                    if s[l] not in m:
                        l += 1
                    else:
                        m[s[l]] -= 1
                        l += 1

                if r - l < length:
                    length = r - l
                    left, right = l, r

        return s[left:right + 1]

if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))