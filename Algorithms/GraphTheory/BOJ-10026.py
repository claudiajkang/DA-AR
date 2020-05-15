from sys import stdin
from copy import deepcopy
from collections import deque
read = lambda: stdin.readline().rstrip()

n = int(read())
rgba = [['x'] + [0] * n + ['x'] for i in range(n+2)]
rgba[0] = ['x'] * (n + 2)
rgba[-1] = ['x'] * (n + 2)
rba = deepcopy(rgba)

for i in range(1, n+1):
    t = read()
    rgba[i] = ['x'] + list(t) + ['x']
    rba[i] = ['x'] + list(t.replace('G', 'R')) + ['x']

rgb = ['R', 'G', 'B']
rb = ['R', 'B']

p = [[0, 1], [0, -1], [1, 0], [-1, 0]]

res_rgb = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if rgba[i][j] in rgb:
            q = deque()
            q.append([i, j])
            cur = rgba[i][j]
            rgba[i][j] = 'D'
            res_rgb += 1

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    if rgba[ci+ii][cj+jj] == cur:
                        rgba[ci+ii][cj+jj] = 'D'
                        q.append([ci+ii, cj+jj])

res_rb = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if rba[i][j] in rb:
            q = deque()
            q.append([i, j])
            cur = rba[i][j]
            rba[i][j] = 'D'
            res_rb += 1

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    if rba[ci+ii][cj+jj] == cur:
                        rba[ci+ii][cj+jj] = 'D'
                        q.append([ci + ii, cj + jj])

print("%d %d" % (res_rgb, res_rb))