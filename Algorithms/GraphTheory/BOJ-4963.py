from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

while True:
    w, h = map(int, read().split())

    if [w, h] == [0, 0]: break

    g = [[] for i in range(h)]

    for i in range(h):
        g[i] = list(map(int, read().split()))

    if w == h and h == 1:
        print(g[0][0])
        continue

    visited = [[False] * w for i in range(h)]

    island = 0

    p = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    for i in range(h):
        for j in range(w):
            if g[i][j] == 1 and not visited[i][j]:
                island += 1
                visited[i][j] = True
                q = deque()
                q.append([i, j])

                while q:
                    ch, cw = q.popleft()

                    for hh, ww in p:
                        th = ch + hh
                        tw = cw + ww

                        if th < 0 or tw < 0 or th >= h or tw >= w: continue

                        if g[th][tw] == 1 and not visited[th][tw]:
                            visited[th][tw] = True
                            q.append([th, tw])

    print(island)
