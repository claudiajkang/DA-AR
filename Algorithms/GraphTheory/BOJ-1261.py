from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

w, h = map(int, read().split())
g = [[] for i in range(h)]

for i in range(h):
    g[i] = list(map(int, list(read())))

INF = 1e9
visited = [[False] * w for i in range(h)]
dist = [[INF] * w for i in range(h)]

dist[0][0] = 0
q = []
heappush(q, [dist[0][0], 0, 0])

res = 0
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

while q:
    cost, ch, cw = heappop(q)

    if visited[ch][cw]: continue
    visited[ch][cw] = True

    for hh, ww in p:
        th = hh + ch
        tw = ww + cw

        if th < 0 or th >= h or tw < 0 or tw >= w:
            continue

        if dist[th][tw] > dist[ch][cw] + g[th][tw]:
            dist[th][tw] = dist[ch][cw] + g[th][tw]
            heappush(q, [dist[th][tw], th, tw])

print(dist[h-1][w-1])