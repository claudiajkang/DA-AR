from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())
p = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for tt in range(t):
    w, h = map(int, read().split())

    visited = [[0] * 1000 for i in range(1000)]
    maps = [[] for i in range(1000)]
    q = deque()
    fq = deque()

    for i in range(h):
        maps[i] = list(read())

        for j in range(w):
            if maps[i][j] == '@':
                visited[i][j] = True
                q.append([i, j])

            elif maps[i][j] == '*':
                fq.append([i, j])

    success = False
    result = 0

    while q:
        result += 1

        qsize = len(q)
        for i in range(qsize):
            r, c = q.popleft()

            if maps[r][c] == '*':
                continue

            for ii, jj in p:
                nr = r + ii
                nc = c + jj

                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    success = True
                    break

                if maps[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append([nr, nc])

            if success: break

        if success: break

        qsize = len(fq)

        for i in range(qsize):
            r, c = fq.popleft()

            for ii, jj in p:
                nr = r + ii
                nc = c + jj

                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    continue

                if maps[nr][nc] == '.':
                    maps[nr][nc] = '*'
                    fq.append([nr, nc])

    if success:
        print(result)
    else:
        print("IMPOSSIBLE")