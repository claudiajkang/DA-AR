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
                visited[i][j] = True
                s.append([i, j])
            elif g[i][j] == '*':
                f.append([i, j])

    time = 0
    suc = False
    p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while s:
        time += 1
        qsize = len(s)

        for i in range(qsize):
            ch, cw = s.popleft()

            if g[ch][cw] == '*': continue

            for hh, ww in p:
                th = hh + ch
                tw = ww + cw

                if th < 0 or tw < 0 or th >= h or tw >= w:
                    suc = True
                    break

                if g[th][tw] == '.' and not visited[th][tw]:
                    visited[th][tw] = True
                    s.append([th, tw])

            if suc: break

        if suc: break

        qsize = len(f)

        for i in range(qsize):
            ch, cw = f.popleft()

            for hh, ww in p:
                th = hh + ch
                tw = ww + cw

                if th < 0 or tw < 0 or th >= h or tw >= w:
                    continue

                if g[th][tw] == '.':
                    f.append([th, tw])
                    g[th][tw] = '*'

    if suc:
        print(time)
    else:
        print("IMPOSSIBLE")
