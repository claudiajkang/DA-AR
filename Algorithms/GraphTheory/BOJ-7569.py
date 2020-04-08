from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

m, n, h = map(int, read().split())
box = [[[0] * m for i in range(n)] for k in range(h)]
tomato = deque()
minus = 0
zero = 0

for hh in range(h):
    for nn in range(n):
        box[hh][nn] = list(map(int, read().split()))

        if box[hh][nn].count(1) > 0:
            for mm in range(m):
                if box[hh][nn][mm] == 1:
                    tomato.append([hh, nn, mm])

        minus += box[hh][nn].count(-1)
        zero += box[hh][nn].count(0)

if (minus + len(tomato)) == (h * n * m):
    print(0)
    exit()

p = [[1, 0, 0], [-1, 0, 0], [0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0]]
res = 0

while tomato:
    ch, cn, cm = tomato.popleft()

    for hh, nn, mm in p:
        th, tn, tm = hh + ch, nn + cn, mm + cm
        if (th < 0 or th >= h) or (tn < 0 or tn >= n) or (tm < 0 or tm >= m):
            continue
        if box[th][tn][tm] == 0:
            tomato.append([th, tn, tm])
            box[th][tn][tm] = box[ch][cn][cm] + 1
            if box[ch][cn][cm] + 1 > res:
                res = box[ch][cn][cm] + 1

for hh in range(h):
    for nn in range(n):
        if box[hh][nn].count(0) > 0:
            res = -1
            break
    if res == -1:
        break

print(res if res == -1 else res - 1)