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

        if ok_len != len(m):
            return ""

        return s[left:right + 1]


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        need = dict()
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        need_cnt = len(t)
        res = ""
        length = len(s)

        l = 0
        for r, c in enumerate(s):
            if c in need:
                if need[c] > 0:
                    need_cnt -= 1
                need[c] -= 1

            while need_cnt == 0:
                if r - l < length:
                    length = r - l
                    res = s[l:r + 1]

                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        need_cnt = need[s[l]]
                l += 1

        return res


if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
