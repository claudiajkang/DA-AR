from collections import deque
from copy import deepcopy
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())

result = ""
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def dfs(i, j, g):
    global c, r

    q = deque()
    q.append([i, j])
    g[i][j] = 0
    mi, mj = 0, 0
    m = 0

    while q:
        ci, cj = q.popleft()

        for ii, jj in p:
            ti = ci + ii
            tj = cj + jj

            if (ti < 0 or ti >= r) or (tj < 0 or tj >= c):
                continue

            if g[ti][tj] == '.':
                g[ti][tj] = g[ci][cj] + 1
                q.append([ti, tj])
                if g[ti][tj] > m:
                    m = g[ti][tj]
                    mi, mj = ti, tj

    return mi, mj, m


for tt in range(t):
    c, r = map(int, read().split())

    g = [['#'] * c for i in range(r)]
    q = deque()
    res = 0
    counts = 0
    initi, initj = 0, 0

    for i in range(r):
        g[i] = ['#'] + list(read()) + ['#']

        if [initi, initj] == [0, 0] and g[i].count('.') > 0:
            initi = i
            initj = g[i].index('.')

        counts += g[i].count('.')

    if counts > 1:
        g2 = deepcopy(g)
        fi, fj, f = dfs(initi, initj, g)
        si, sj, res = dfs(fi, fj, g2)

    else:
        res = 0

    result += f'Maximum rope length is {res}.\n'

print(result[:-1], end="")
