#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/29

def sample(m, n):
    if n == 0:
        return 1
    dp = [1] * m
    for _ in range(1, n):
        nesDp = []
        for i in range(m):
            nesDp.append(sum(dp[:i + 1]))
        dp = nesDp
    return sum(dp)


while True:
    nums = input()
    if not nums:
        break
    nums = nums.split()
    m = int(nums[0])
    n = int(nums[1])
    res = ''
    for i in range(m,n+1):
        if i == (i%10)**3 + (i//10%10)**3 + (i//100%10)**3:
            res += (str(i) + ' ')
    print(res)
