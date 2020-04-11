from collections import deque
from copy import deepcopy
from sys import stdin

read = lambda: stdin.readline().rstrip()

def dfs(pos):
    global g, c, r

    q = deque()
    q.append(pos)
    g[pos[0]][pos[1]] = 0
    mpos = [0, 0]
    m = 0

    while q:
        ci, cj = q.popleft()

        for ii, jj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ti, tj = ii + ci, jj + cj

            if (0 <= ti <= r) and (0 <= tj <= c):
                if g[ti][tj] == '.':
                    g[ti][tj] = g[ci][cj] + 1
                    q.append([ti, tj])
                    if g[ti][tj] > m:
                        m = g[ti][tj]
                        mpos = [ti, tj]

    return mpos, m


t = int(read())

for tt in range(t):
    c, r = map(int, read().split())
    g = [[0] * c for i in range(r)]
    start = [0, 0]

    for i in range(r):
        g[i] = list(read())

        if start == [0, 0] and '.' in g[i]:
            start = [i, g[i].index('.')]

    g1 = deepcopy(g)
    fpos, f = dfs(start)
    g = g1
    spos, s = dfs(fpos)

    print(f"Maximum rope length is {s}.")
