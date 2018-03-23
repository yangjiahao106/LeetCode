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


if __name__ == '__main__':
    res = fibonacci(3)
    print(res)
