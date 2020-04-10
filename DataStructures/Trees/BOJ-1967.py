from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()


def dfs(num):
    global g

    visited = [-1] * len(g)
    visited[num] = 0
    q = deque()
    q.append(num)
    mi, m = 0, 0

    while q:
        cur = q.popleft()

        for idx, val in g[cur]:
            if visited[idx] == -1:
                visited[idx] = visited[cur] + val
                q.append(idx)
                if visited[idx] > m:
                    m = visited[idx]
                    mi = idx

    return mi, m


n = int(read())
g = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, read().split())
    g[a].append([b, c])
    g[b].append([a, c])

fi, f = dfs(1)
si, s = dfs(fi)

print(s)
