from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    w, h = map(int, read().split())

    b = [[] for i in range(h)]
    visited = [[False] * w for i in range(h)]
    fire = deque()
    pos = deque()

    for i in range(h):
        b[i] = list(read())

        for j in range(w):
            if b[i][j] == '*':
                fire.append([i, j])
            elif b[i][j] == '@':
                pos.append([i, j])
                visited[i][j] = True

    p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    time = 0
    suc = False

    while pos:
        time += 1

        qsize = len(pos)

        for i in range(qsize):
            ch, cw = pos.popleft()

            if b[ch][cw] == '*': continue

            for hh, ww in p:
                th, tw = ch + hh, cw + ww
                if th < 0 or th >= h or tw < 0 or tw >= w:
                    suc = True
                    break

                if b[th][tw] == '.' and not visited[th][tw]:
                    visited[th][tw] = True
                    pos.append([th, tw])

            if suc: break

        if suc: break

        qsize = len(fire)
        for i in range(qsize):
            ch, cw = fire.popleft()

            for hh, ww in p:
                th, tw = ch + hh, cw + ww
                if th < 0 or th >= h or tw < 0 or tw >= w:
                    continue

                if b[th][tw] == '.':
                    fire.append([th, tw])
                    b[th][tw] = '*'

    if suc:
        print(time)
    else:
        print("IMPOSSIBLE")
