from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

while True:
    l, h, w = map(int, read().split())

    if [l, h, w] == [0, 0, 0]: break

    g = [[[] for i in range(h)] for k in range(l)]
    q = deque()

    for i in range(l):
        for j in range(h):
            g[i][j] = list(read())
            if 'S' in g[i][j]: q.append([i, j, g[i][j].index('S')])

        t = read()

    p = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0]]
    suc = False
    g[q[0][0]][q[0][1]][q[0][2]] = 0
    time = 0

    while q:
        cl, ch, cw = q.popleft()

        for ll, hh, ww in p:
            tl = ll + cl
            th = hh + ch
            tw = ww + cw

            if (0 <= tl < l) and (0 <= th < h) and (0 <= tw < w):
                if g[tl][th][tw] == 'E':
                    suc = True
                    time = g[cl][ch][cw] + 1
                    break

                if g[tl][th][tw] == '.':
                    g[tl][th][tw] = g[cl][ch][cw] + 1
                    q.append([tl, th, tw])

    if suc:
        print(f'Escaped in {time} minute(s).')
    else:
        print("Trapped!")
