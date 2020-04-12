from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    l = [0] + list(map(int, read().split()))

    for j in range(1, n + 1):
        if l[j] == 1:
            g[i].append(j)

result = [[-1] * (n + 1) for i in range(n + 1)]
visited = [[False] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if result[i][j] == -1:
            q = deque()
            q.append(i)
            dfs = []
            init = False if i == j else True
            err = True

            while q:
                cur = q.popleft()

                if init and cur == j:
                    result[i][j] = 1
                    err = False
                    break

                if not init: init = True

                for k in g[cur]:
                    if k not in dfs:
                        result[cur][k] = 1
                        result[i][k] = 1
                        q.append(k)
                        dfs.append(k)

            if err:
                result[i][j] = 0

for i in range(1, n + 1):
    print(' '.join(map(str, result[i][1:])))
