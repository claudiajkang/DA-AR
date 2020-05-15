from collections import deque
from sys import stdin

read = lambda: stdin.readline()

T = int(read())

for tt in range(T):
    n = int(read())
    g = [[] for i in range(n + 1)]
    temp = [0] + list(map(int, read().split()))

    for i in range(1, n + 1):
        g[temp[i]].append(i)

    visited = [False for i in range(n + 1)]
    res = 0

    for i in range(1, n + 1):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = True

            while q:
                cur = q.popleft()

                for j in g[cur]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)

            res += 1

    print(res)
