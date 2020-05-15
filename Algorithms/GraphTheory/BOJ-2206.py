from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

h, w = map(int, read().split())
g = [[] for i in range(h)]

for i in range(h):
    g[i] = list(map(int, list(read())))

q = deque()
q.append([0, 0, 0])
visited = [[[False] * w for i in range(h)] for j in range(2)]

time = 0
suc = False
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

while q:
    time += 1

    qlen = len(q)
    for i in range(qlen):
        crash, ch, cw = q.popleft()

        if ch == (h - 1) and cw == (w - 1):
            suc = True
            break

        for hh, ww in p:
            th = hh + ch
            tw = ww + cw

            if th < 0 or tw < 0 or th >= h or tw >= w:
                continue

            if g[th][tw] == 1:
                if crash:
                    continue
                else:
                    if not visited[1][th][tw]:
                        visited[1][th][tw] = True
                        q.append([1, th, tw])

            if g[th][tw] == 0:
                if not visited[crash][th][tw]:
                    visited[crash][th][tw] = True
                    q.append([crash, th, tw])

    if suc: break

if suc:
    print(time)
else:
    print(-1)
