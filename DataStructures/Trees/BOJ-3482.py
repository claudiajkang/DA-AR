from collections import deque
from copy import deepcopy
from sys import stdin

read = lambda: stdin.readline().rstrip()


def dfs(start, g):
    global c, r

    q = deque()
    q.append(start)
    g[start[0]][start[1]] = 0
    midx = [0, 0]
    m = 0

    while q:
        ci, cj = q.popleft()
        for ii, jj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            ti = ci + ii
            tj = cj + jj

            if (0 <= ti < r) and (0 <= tj < c):
                if g[ti][tj] == '.':
                    g[ti][tj] = g[ci][cj] + 1
                    q.append([ti, tj])
                    if g[ti][tj] > m:
                        m = g[ti][tj]
                        midx = [ti, tj]

    return midx, m


t = int(read())
result = ""

for tt in range(t):
    c, r = map(int, read().split())

    g = [[] for i in range(r)]
    init = False
    start = [-1, -1]

    for i in range(r):
        g[i] = list(read())

        if not init and g[i].count('.') > 0:
            start = [i, g[i].index('.')]
            init = True

    g2 = deepcopy(g)
    fidx, fm = dfs(start, g)
    sidx, sm = dfs(fidx, g2)

    result += f"Maximum rope length is {sm}.\n"

print(result[:-1], end="")
