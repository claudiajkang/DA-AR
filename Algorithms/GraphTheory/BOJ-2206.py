from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
maps = [[] for i in range(n)]
for i in range(n):
    maps[i] = list(map(int, list(read())))

visited = [[[False] * m for i in range(n)] for ii in range(2)]
visited[0][0][0] = True
q = deque()
q.append([0, 0, 0])
result = 1

while q:
    qsize = len(q)
    reach = False

    for i in range(qsize):
        crash, r, c = q.popleft()

        if r == (n - 1) and c == (m - 1):
            reach = True
            break

        for rr, cc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = r + rr, c + cc

            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue

            if visited[crash][nr][nc]: continue

            if maps[nr][nc] and crash:
                continue

            elif maps[nr][nc] and not crash:
                visited[1][nr][nc] = True
                q.append([1, nr, nc])

            else:
                visited[crash][nr][nc] = True
                q.append([crash, nr, nc])

    if reach: break

    result += 1

print(result if visited[0][n - 1][m - 1] or visited[1][n - 1][m - 1] else -1)
