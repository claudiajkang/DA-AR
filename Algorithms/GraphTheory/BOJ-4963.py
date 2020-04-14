from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n)]
res = [[-1] * n for i in range(n)]

for i in range(n):
    l = list(map(int, read().split()))

    for j in range(n):
        if l[j] == 1:
            g[i].append(j)

for i in range(n):
    for j in range(n):
        if res[i][j] == -1:
            q = deque()
            q.append(i)
            dfs = []
            init = False if i == j else True

            while q:
                cur = q.popleft()

                if cur == j and init:
                    res[i][j] = 1
                    break

                if not init: init = True

                for k in g[cur]:
                    if k not in dfs:
                        q.append(k)
                        dfs.append(k)
                        res[cur][k] = 1
                        res[i][k] = 1

            if res[i][j] == -1:
                res[i][j] = 0

for i in range(n):
    print(' '.join(map(str, res[i])))
