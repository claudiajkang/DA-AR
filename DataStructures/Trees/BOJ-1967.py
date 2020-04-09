from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, read().split())
    g[a].append([b, c])
    g[b].append([a, c])


def dfs(nnum):
    global g

    q = deque()
    q.append([nnum, 0])
    d = 0
    di = 0
    visited = [False] * (n + 1)
    visited[nnum] = True

    while q:
        cur, cd = q.popleft()

        for jj, jd in g[cur]:
            if not visited[jj]:
                q.append([jj, cd + jd])
                visited[jj] = True
                if (cd + jd) > d:
                    d = cd + jd
                    di = jj

    return di, d


fidx, fv = dfs(1)
sidx, sv = dfs(fidx)

print(sv)
