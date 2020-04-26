from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def dfs(h, w):
    global g, visited, A, cnt, q, p, n

    visited[h][w] = True
    A[h][w] = cnt
    q.append([h, w])

    for hh, ww in p:
        th = h + hh
        tw = w + ww

        if th < 0 or tw < 0 or th >= n or tw >= n:
            continue

        if not visited[th][tw] and g[th][tw]:
            dfs(th, tw)


n = int(read())
g = [[0] * n for i in range(n)]
A = [[0] * n for i in range(n)]

for i in range(n):
    g[i] = list(map(int, read().split()))

cnt = 0
q = deque()
visited = [[False] * n for i in range(n)]
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and g[i][j]:
            cnt += 1
            dfs(i, j)

res = 1

while True:
    qlen = len(q)

    for i in range(qlen):
        h, w = q.popleft()

        for hh, ww in p:
            th = h + hh
            tw = w + ww

            if th < 0 or tw < 0 or th >= n or tw >= n:
                continue

            if not visited[th][tw]:
                visited[th][tw] = True
                A[th][tw] = A[h][w]
                q.append([th, tw])

            elif A[th][tw] != A[h][w]:
                print(res)
                exit()

    res += 1

    con = False

    for i in range(n):
        for j in range(n):
            if A[i][j] != 0:
                for ii, jj in p:
                    ti = ii + i
                    tj = jj + j

                    if ti < 0 or tj < 0 or ti >= n or tj >= n:
                        continue

                    if A[ti][tj] != 0 and A[ti][tj] != A[i][j]:
                        print(res)
                        exit()

    res += 1
