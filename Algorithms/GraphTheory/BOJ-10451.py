from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

tt = int(read())

for t in range(tt):
    n = int(read())

    arr = [0] + list(map(int, read().split()))
    g = [[] for i in range(n+1)]

    for i in range(1, n+1):
        g[i].append(arr[i])

    visited = [False] * (n+1)
    res = 0

    for i in range(1, n+1):
        if not visited[i]:
            q = deque()
            dfs = deque()
            q.append(i)
            dfs.append(i)

            while q:
                c = q.popleft()

                for j in g[c]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
                        if j not in dfs:
                            dfs.append(j)

            if dfs:
                res += 1

    print(res)
