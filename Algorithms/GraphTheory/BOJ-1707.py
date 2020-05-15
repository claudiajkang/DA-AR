from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

k = int(read())

for t in range(k):
    v, e = map(int, read().split())
    g = [[] for i in range(v + 1)]

    for i in range(e):
        a, b = map(int, read().split())
        g[a].append(b)
        g[b].append(a)

    visited = [''] * (v + 1)
    color = ['R', 'G']
    colorIdx = False
    err = False

    for i in range(1, v + 1):
        if visited[i] == '':
            visited[i] = color[not colorIdx]
            q = deque()
            q.append(i)

            while q:
                cur = q.popleft()
                cidx = color.index(visited[cur])

                for j in g[cur]:
                    if visited[j] == '':
                        visited[j] = color[not cidx]
                        q.append(j)
                        continue

                    if i != j and visited[j] != color[not cidx]:
                        err = True
                        break

                if err:
                    break

            if err:
                break

    print(['YES', 'NO'][err])
