#! python3
# __author__ = "YangJiaHao"
# date: 2018/12/25

# 动态规划 O(n^2)
def max_product_after_cutting(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    products = [0, 1, 2, 3]

    for i in range(4, n + 1):
        max = 0
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if product > max:
                max = product

        products.append(max)

    return products[n]


def max_product_after_cutting2(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    res = 1

    while n > 5:
        n -= 3
        res *= 3

    return res * n
