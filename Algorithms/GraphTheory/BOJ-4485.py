from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

INF = 1e9
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
case = 1
while True:
    n = int(read())

    if n == 0: break

    g = [[] for i in range(n)]

    for i in range(n):
        g[i] = list(map(int, read().split()))

    visited = [[False] * n for i in range(n)]
    dist = [[INF] * n for i in range(n)]

    dist[0][0] = g[0][0]
    q = []
    heappush(q, [dist[0][0], 0, 0])

    while q:
        cost, ci, cj = heappop(q)

        if visited[ci][cj]: continue

        visited[ci][cj] = True

        for ii, jj in p:
            ti = ii + ci
            tj = jj + cj

            if ti < 0 or ti >= n or tj < 0 or tj >= n:
                continue

            if dist[ti][tj] > dist[ci][cj] + g[ti][tj]:
                dist[ti][tj] = dist[ci][cj] + g[ti][tj]
                heappush(q, [dist[ti][tj], ti, tj])

    print(f"Problem {case}: {dist[n - 1][n - 1]}")
    case += 1
