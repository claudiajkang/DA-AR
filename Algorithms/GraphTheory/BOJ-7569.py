from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

m, n, h = map(int, read().split())

box = [[[0] * m for i in range(n)] for _ in range(h)]
q = deque()
zero = 0
minus = 0

for hh in range(h):
    for i in range(n):
        box[hh][i] = list(map(int, read().split()))

        if box[hh][i].count(1) > 0:
            for j in range(m):
                if box[hh][i][j] == 1:
                    q.append([hh, i, j])

        zero += box[hh][i].count(0)
        minus += box[hh][i].count(-1)

if zero == 0 and (len(q) + minus == (h * m * n)):
    print(0)
    exit()

p = [[1, 0, 0], [-1, 0, 0], [0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0]]
res = 0

while q:
    ch, ci, cj = q.popleft()

    for hh, ii, jj in p:
        th = hh + ch
        ti = ii + ci
        tj = jj + cj

        if (th < 0 or th >= h) or (ti < 0 or ti >= n) or (tj < 0 or tj >= m):
            continue

        if box[th][ti][tj] == 0:
            if (box[ch][ci][cj] + 1) > res:
                res = box[ch][ci][cj] + 1

            box[th][ti][tj] = box[ch][ci][cj] + 1
            q.append([th, ti, tj])

for hh in range(h):
    for i in range(n):
        if box[hh][i].count(0) > 0:
            res = -1

print(res if res == -1 else res - 1)
