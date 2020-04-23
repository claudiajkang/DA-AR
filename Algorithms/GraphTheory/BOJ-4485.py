from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

case = 1
while True:
    n = int(read())
    if n == 0: break

    g = [[] for i in range(n)]

    for i in range(n):
        g[i] = list(map(int, read().split()))

    INF = 1e9

    dist = [[INF] * n for i in range(n)]
    visited = [[False] * n for i in range(n)]

    dist[0][0] = g[0][0]
    q = []
    heappush(q, [dist[0][0], 0, 0])

    p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    while q:
        cost, ch, cw = heappop(q)

        if visited[ch][cw]:
            continue

        visited[ch][cw] = True

        for hh, ww in p:
            th = ch + hh
            tw = cw + ww

            if th < 0 or tw < 0 or th >= n or tw >= n:
                continue

            if dist[th][tw] > dist[ch][cw] + g[th][tw]:
                dist[th][tw] = dist[ch][cw] + g[th][tw]
                heappush(q, [dist[th][tw], th, tw])

    print(f"Problem {case}: {dist[n - 1][n - 1]}")
    case += 1