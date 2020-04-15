from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

h, w = map(int, read().split())
g = [[] for i in range(h)]
visited = [[False] * w for i in range(h)]
wt = deque()
s = deque()

for i in range(h):
    g[i] = list(read())

    for j in range(w):
        if g[i][j] == 'S':
            visited[i][j] = True
            s.append([i, j])
            g[i][j] = '.'

        if g[i][j] == '*':
            wt.append([i, j])

time = 0
suc = False
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
while s:
    qlen = len(s)

    time += 1

    for i in range(qlen):
        ch, cw = s.popleft()

        if g[ch][cw] == '*': continue

        for hh, ww in p:
            th = ch + hh
            tw = cw + ww

            if th < 0 or tw < 0 or th >= h or tw >= w:
                continue

            if g[th][tw] == 'D':
                suc = True
                break

            if g[th][tw] == '.' and not visited[th][tw]:
                visited[th][tw] = True
                s.append([th, tw])

        if suc: break

    if suc: break

    qlen = len(wt)

    for i in range(qlen):
        ch, cw = wt.popleft()

        for hh, ww in p:
            th = ch + hh
            tw = cw + ww

            if th < 0 or tw < 0 or th >= h or tw >= w:
                continue

            if g[th][tw] == '.':
                g[th][tw] = '*'
                wt.append([th, tw])

if suc:
    print(time)
else:
    print('KAKTUS')
