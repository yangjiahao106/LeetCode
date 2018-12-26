#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/23


def fibonacci(n):
    res = [0, 1]

    if n <= 1:
        return res[n]

    for i in range(1, n):
        res[0], res[1] = res[1], res[0] + res[1]

    return res[1]


# 递归方式，效率较低。
def fibonacci_re(n):
    if n <= 0 :
        return 0

    if n ==1:
        return 1

    return fibonacci_re(n-1) + fibonacci_re(n-2)

# 青蛙跳台阶问题
pass

# 青蛙变态跳台阶问题，一次可以跳n阶台阶

def abnormal_frog(n):
    if n <= 1:
        return n

    return 2 ** (n-1)





if __name__ == '__main__':
    res = fibonacci(3)
    print(res)
