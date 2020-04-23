from heapq import heappop, heappush
from sys import stdin

read = lambda: stdin.readline().rstrip()

w, h = map(int, read().split())
g = [[] for i in range(h)]

for i in range(h):
    g[i] = list(map(int, list(read())))

p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

INF = 1e9
dist = [[INF] * w for i in range(h)]
visited = [[False] * w for i in range(h)]

dist[0][0] = 0
q = []
heappush(q, [dist[0][0], 0, 0])

while q:
    cost, ch, cw = heappop(q)

    if visited[ch][cw]: continue
    visited[ch][cw] = True

    for hh, ww in p:
        th = ch + hh
        tw = cw + ww

        if th < 0 or tw < 0 or th >= h or tw >= w:
            continue

        if dist[th][tw] > dist[ch][cw] + g[th][tw]:
            dist[th][tw] = dist[ch][cw] + g[th][tw]
            heappush(q, [dist[th][tw], th, tw])

print(dist[h-1][w-1])