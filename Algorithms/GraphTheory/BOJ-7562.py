from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())
res = []
px = (2, 1, -1, -2, -2, -1, 1, 2)
py = (1, 2, 2, 1, -1, -2, -2, -1)


def bfs():
    global dx, dy, b, l

    q = deque()
    q.append([cx, cy])

    while q:
        ci, cj = q.popleft()
        if ci == dx and cj == dy:
            print(b[ci][cj])
            break

        for idx in range(8):
            ti = ci + px[idx]
            tj = cj + py[idx]

            if ti < 0 or ti >= l or tj < 0 or tj >= l:
                continue
            if not b[ti][tj]:
                b[ti][tj] = b[ci][cj] + 1
                q.append([ti, tj])


for tt in range(t):
    l = int(read())
    b = [[0] * l for i in range(l)]
    cx, cy = map(int, read().split())
    dx, dy = map(int, read().split())
    bfs()
