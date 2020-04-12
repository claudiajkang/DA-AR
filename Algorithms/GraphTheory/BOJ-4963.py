from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

while True:
    w, h = map(int, read().split())

    if w == 0 and h == 0:
        break

    g = [[] for i in range(h)]

    for i in range(h):
        g[i] = list(map(int, read().split()))

    if w == 1 and h == 1:
        print(0 if g[0][0] == 0 else 1)
        continue

    visited = [[False] * w for i in range(h)]

    res = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] == 1 and not visited[i][j]:
                q = deque()
                visited[i][j] = True
                q.append([i, j])

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in [[-1, -1], [-1, 1], [-1, 0], [1, 0], [0, -1], [0, 1], [1, -1], [1, 1]]:
                        ti = ci + ii
                        tj = cj + jj

                        if ti < 0 or ti >= h or tj < 0 or tj >= w:
                            continue

                        if g[ti][tj] == 1 and not visited[ti][tj]:
                            visited[ti][tj] = True
                            q.append([ti, tj])

                res += 1

    print(res)
