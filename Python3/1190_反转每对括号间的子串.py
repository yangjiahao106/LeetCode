class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        for c in s:
            if c == ')':
                subs = []
                while True:
                    c = stack.pop()
                    if c == '(':
                        stack += subs
                        break
                    else:
                        subs.append(c)
            else:
                stack.append(c)

        return "".join(stack)


class Solution2:
    """ 从内向外依次反转， 和从外向内依次反转的结果时一样的
    (ed(et(oc))el) -> (ed(et(co))el) -> (ed((oc)te)el) -> (le(et(co))de)
    (ed(et(oc))el) -> (le((co)te)de) -> (le(et(oc))de) -> (le(et(co))de)
    """

    def reverseParentheses(self, s: str) -> str:
        pair = dict()
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue
            if s[i] == ')':
                l_idx = stack.pop()
                pair[l_idx] = i
                pair[i] = l_idx

        step = 1
        pos = 0
        res = []

        print(pair)
        while pos < len(s):
            if s[pos] == '(' or s[pos] == ')':
                pos = pair[pos]
                step = - step
            else:
                res.append(s[pos])
            pos += step

        return "".join(res)


if __name__ == '__main__':
    print(Solution2().reverseParentheses("(abc)"))
