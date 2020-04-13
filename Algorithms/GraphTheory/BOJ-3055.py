from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

h, w = map(int, read().split())
g = [[] for i in range(h)]
S = deque()
WT = deque()
visited = [[False] * w for i in range(h)]

for i in range(h):
    g[i] = list(read())

    for j in range(w):
        if g[i][j] == 'S':
            S.append([i, j])
            visited[i][j] = True
            g[i][j] = '.'
        elif g[i][j] == '*':
            WT.append([i, j])

time = 0
suc = False
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

while S:
    time += 1
    qlen = len(S)

    for i in range(qlen):
        ch, cw = S.popleft()

        if g[ch][cw] == '*':
            continue

        for hh, ww in p:
            th = ch + hh
            tw = cw + ww

            if th < 0 or th >= h or tw < 0 or tw >= w:
                continue

            if g[th][tw] == '.' and not visited[th][tw]:
                S.append([th, tw])
                visited[th][tw] = True

            if g[th][tw] == 'D':
                suc = True
                break

        if suc: break

    if suc: break

    qlen = len(WT)

    for i in range(qlen):
        ch, cw = WT.popleft()

        for hh, ww in p:
            th = ch + hh
            tw = cw + ww

            if th < 0 or th >= h or tw < 0 or tw >= w:
                continue

            if g[th][tw] == '.':
                g[th][tw] = '*'
                WT.append([th, tw])

if suc:
    print(time)
else:
    print('KAKTUS')
