# Floyd 算法


# 求得任意两点的最短路径，这称为“多源最短路”
def floyd():
    inf = 1 << 31
    # d 一定是个邻接矩阵 代表任意两点之间的距离 inf 表示不能到达
    d = [
        [0, 2, 6, 4],
        [inf, 0, 3, inf],
        [7, inf, 0, 1],
        [5, inf, 12, 0]
    ]

    n = len(d)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 如果通过K点中转距离更短，则更新最短距离
                # 核心思想是 "动态规划"
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    # 结果为任意两点之间的最短距离
    for r in d:
        print(r)


# 戴克斯特拉演算法, 求单源最短路径
def dijkstra():
    inf = 1 << 31
    d = [
        [0, 1, 12, inf, inf, inf],
        [inf, 0, 9, 3, inf, inf],
        [inf, inf, 0, inf, 5, inf],
        [inf, inf, 4, 0, 13, 15],
        [inf, inf, inf, inf, 0, 4],
        [inf, inf, inf, inf, inf, 0],

    ]

    # 0 —> 5 距离
    start = 0
    end = 5

    dp = d[start][:]  # 记录到各个点的最短距离
    dp[start] = inf
    print(dp)
    res = d[start][:]
    while True:
        # find smallest v
        smallest_idx = 0
        smallest_dis = inf

        for idx, dis in enumerate(dp):
            if dis < smallest_dis:
                smallest_dis = dis
                smallest_idx = idx

        res[smallest_idx] = smallest_dis

        if smallest_idx == end:
            print("Find", smallest_dis)
            print(res)

            return

        dp[smallest_idx] = inf  # 标记删除

        for v, dis in enumerate(d[smallest_idx]):
            if v == smallest_idx or dis == inf:  # 跳过自己
                continue

            if smallest_dis + dis < dp[v]:
                dp[v] = smallest_dis + dis



if __name__ == '__main__':
    dijkstra()
