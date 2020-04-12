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

res = [[0] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        q = deque()
        q.append(i)
        dfs = []
        flag = False
        if i == j:
            init = False
        else:
            init = True
        while q:
            cur = q.popleft()

            if cur == j and init:
                flag = True
                break

            if i == j and not init:
                init = True

            for t in g[cur]:
                if t not in dfs:
                    q.append(t)
                    dfs.append(t)

        res[i][j] = 1 if flag else 0

for i in range(1, n + 1):
    print(' '.join(map(str, res[i][1:])))
