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

    res = 0
    visited = [[False] * w for i in range(h)]

    for i in range(h):
        for j in range(w):
            if g[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = True

                while q:
                    ch, cw = q.popleft()

                    for hh, ww in [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                        th = ch + hh
                        tw = cw + ww

                        if th < 0 or tw < 0 or th >= h or tw >= w:
                            continue

                        if g[th][tw] == 1 and not visited[th][tw]:
                            q.append([th, tw])
                            visited[th][tw] = True
                            g[th][tw] = 0

                res += 1

    print(res)
