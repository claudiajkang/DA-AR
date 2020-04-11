from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    w, h = map(int, read().split())

    g = [[] for i in range(h)]
    visited = [[False] * w for i in range(h)]

    f = deque()
    s = deque()

    for i in range(h):
        g[i] = list(read())

        for j in range(w):
            if g[i][j] == '@':
                s.append([i, j])
                visited[i][j] = True

            elif g[i][j] == '*':
                f.append([i, j])

    p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    suc = False
    time = 0

    while s:
        time += 1
        qsize = len(s)

        for i in range(qsize):
            ch, cw = s.popleft()

            if g[ch][cw] == '*':
                continue

            for ww, hh in p:
                tw = ww + cw
                th = hh + ch

                if tw < 0 or tw >= w or th < 0 or th >= h:
                    suc = True
                    break

                if g[th][tw] == '.' and not visited[th][tw]:
                    s.append([th, tw])
                    visited[th][tw] = True

            if suc: break

        if suc: break

        qsize = len(f)

        for i in range(qsize):
            ch, cw = f.popleft()

            for ww, hh in p:
                tw = ww + cw
                th = hh + ch

                if tw < 0 or tw >= w or th < 0 or th >= h:
                    continue

                if g[th][tw] == '.':
                    f.append([th, tw])
                    g[th][tw] = '*'

    if suc:
        print(time)
    else:
        print("IMPOSSIBLE")
