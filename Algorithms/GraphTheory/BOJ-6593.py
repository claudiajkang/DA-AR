from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

while True:
    l, h, w = map(int, read().split())

    if [l, h, w] == [0, 0, 0]:
        break

    g = [[[] for i in range(h)] for j in range(l)]
    q = deque()

    for ll in range(l):
        for hh in range(h):
            g[ll][hh] = list(read())
            if 'S' in g[ll][hh]:
                t = g[ll][hh].index('S')
                q.append([ll, hh, t])
                g[ll][hh][t] = 0

        tp = read()

    p = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]
    res = 0
    suc = False

    while q:
        cl, ch, cw = q.popleft()

        for ll, hh, ww in p:
            tl = ll + cl
            th = hh + ch
            tw = ww + cw

            if tl < 0 or tl >= l or th < 0 or th >= h or tw < 0 or tw >= w:
                continue

            if g[tl][th][tw] == 'E':
                suc = True
                res = g[cl][ch][cw] + 1
                break

            if g[tl][th][tw] == '.':
                g[tl][th][tw] = g[cl][ch][cw] + 1
                q.append([tl, th, tw])

        if suc: break

    if suc:
        print(f"Escaped in {res} minute(s).")
    else:
        print('Trapped!')
