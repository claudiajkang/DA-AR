from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

while True:
    w, h = read()

    if w == 0 and h == 0: break

    g = [[] for i in range(h)]
    for i in range(h):
        g[i] = list(read())

    if w == h and h == 1:
        print(g[0][0])
        continue

    l = 0

    for i in range(h):
        for j in range(w):
            if g[i][j] == 1:
                q = deque()
                q.append([i, j])
                g[i][j] = 0

                while q:
                    ch, cw = q.popleft()

                    for hh, ww in [[-1, -1], [-1, 1], [-1, 0], [1, 0], [0, -1], [0, 1], [1, -1], [1, 1]]:
                        th, tw = hh + ch, ww + cw

                        if th < 0 or th >= h or tw < 0 or tw >= w:
                            continue

                        if g[th][tw] == 1:
                            q.append([th, tw])
                            g[th][tw] = 0

                l += 1

    print(l)
