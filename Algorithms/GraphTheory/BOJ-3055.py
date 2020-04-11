from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

h, w = map(int, read().split())
g = [[] for i in range(h)]

dpos = [0, 0]
spos = deque()
water = deque()

visited = [[False] * w for i in range(h)]

for i in range(h):
    g[i] = list(read())

    for j in range(w):
        if g[i][j] == 'D':
            dpos = [i, j]

        elif g[i][j] == 'S':
            spos.append([i, j])
            visited[i][j] = True

        elif g[i][j] == '*':
            water.append([i, j])

suc = False
time = 0
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

while spos:
    time += 1

    qsize = len(water)
    for i in range(qsize):
        ch, cw = water.popleft()

        for hh, ww in p:
            th = ch + hh
            tw = cw + ww

            if th < 0 or th >= h or tw < 0 or tw >= w:
                continue

            if g[th][tw] == '.':
                g[th][tw] = '*'
                water.append([th, tw])

    qsize = len(spos)

    for i in range(qsize):
        ch, cw = spos.popleft()

        for hh, ww in p:
            th = ch + hh
            tw = cw + ww

            if [th, tw] == dpos:
                suc = True
                break

            if th < 0 or th >= h or tw < 0 or tw >= w:
                continue

            if g[th][tw] == '.' and not visited[th][tw]:
                spos.append([th, tw])
                visited[th][tw] = True

        if suc: break

    if suc: break

if suc:
    print(time)
else:
    print('KAKTUS')
