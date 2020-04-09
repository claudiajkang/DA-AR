from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

p = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

result = ''
while True:
    L, R, C = map(int, read().split())

    if [0, 0, 0] == [L, R, C]:
        print(result[:-1])
        break

    g = [[['#'] * (C + 2) for i in range(R + 2)] for t in range(L + 2)]

    start, end = 0, 0

    for ll in range(1, L + 1):
        for rr in range(1, R + 1):
            g[ll][rr] = ['#'] + list(read()) + ['#']

            if g[ll][rr].count('S') > 0:
                start = [ll, rr, g[ll][rr].index('S')]

            if g[ll][rr].count('E') > 0:
                end = [ll, rr, g[ll][rr].index('E')]

        t = read()

    q = deque()
    q.append(start)
    g[start[0]][start[1]][start[2]] = 0
    done = False
    res = 0

    while q:
        curl, curr, curc = q.popleft()

        for ll, rr, cc in p:
            tl, tr, tc = curl + ll, curr + rr, curc + cc

            if [tl, tr, tc] == end:
                g[tl][tr][tc] = g[curl][curr][curc] + 1
                res = g[curl][curr][curc] + 1
                done = True
                break

            if g[tl][tr][tc] == '.':
                g[tl][tr][tc] = g[curl][curr][curc] + 1
                q.append([tl, tr, tc])

        if done:
            break

    for ll in range(1, L + 1):
        for rr in range(1, R + 1):
            if g[ll][rr].count('E'):
                res = -1
                break

        if res == -1:
            break

    if res == -1:
        result += 'Trapped!\n'

    else:
        result += f'Escaped in {res} minute(s).\n'
