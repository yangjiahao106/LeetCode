#! python3
# __author__ = "YangJiaHao"
# date: 2018/12/26
# 1. 两个字符串的交集

def intersection(str1, str2):
    myset = set(str1)
    res = set()
    for c in str2:
        if c in myset:
           res.add(c)

    return res

res = intersection("abcd","kjcb")
print(res)




