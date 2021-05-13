#! python3
# __author__ = "YangJiaHao"
# date: 2018/12/26



def number_of1(n):
    count = 0
    while(n):

        count += 1
        n = (n-1) & n

    return count


if __name__ == '__main__':
    res = number_of1(-1)
    print(res)

