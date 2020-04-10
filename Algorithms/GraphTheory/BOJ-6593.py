from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

result = ""
while True:
    l, r, c = map(int, read().split())

    if [l, r, c] == [0, 0, 0]:
        print(result[:-1], end="")
        break

    g = [[['#'] * c for i in range(r)] for k in range(l)]
    start = [0, 0, 0]
    end = [0, 0, 0]

    for ll in range(l):
        for rr in range(r):
            g[ll][rr] = list(read())

            if 'S' in g[ll][rr]:
                start = [ll, rr, g[ll][rr].index('S')]

            if 'E' in g[ll][rr]:
                end = [ll, rr, g[ll][rr].index('E')]

        temp = read()

    p = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0]]

    g[start[0]][start[1]][start[2]] = 0
    q = deque()
    q.append(start)
    done = False
    res = 0

    while q:
        cur = q.popleft()

        for ll, rr, cc in p:
            tl, tr, tc = cur[0] + ll, cur[1] + rr, cur[2] + cc

            if (0 <= tl < l) and (0 <= tr < r) and (0 <= tc < c):
                if [tl, tr, tc] == end:
                    res = g[cur[0]][cur[1]][cur[2]] + 1
                    done = True
                    break

                if g[tl][tr][tc] == '.':
                    g[tl][tr][tc] = g[cur[0]][cur[1]][cur[2]] + 1
                    q.append([tl, tr, tc])

    if done:
        result += f"Escaped in {res} minute(s).\n"
    else:
        result += f"Trapped!\n"
