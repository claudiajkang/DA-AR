from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n)]

for i in range(n):
    l = list(map(int, read().split()))
    for j in range(n):
        if l[j] == 1:
            g[i].append(j)

result = [[-1] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if result[i][j] == -1:
            q = deque()
            q.append(i)
            init = False if i == j else True
            dfs = []

            while q:
                cur = q.popleft()

                if init and cur == j:
                    result[i][j] = 1
                    break

                if not init:
                    init = True

                for k in g[cur]:
                    if k not in dfs:
                        result[i][k] = 1
                        result[cur][k] = 1
                        q.append(k)
                        dfs.append(k)

            if result[i][j] == -1:
                result[i][j] = 0

for i in range(n):
    print(' '.join(map(str, result[i])))
