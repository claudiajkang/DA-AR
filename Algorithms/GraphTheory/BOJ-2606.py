from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

cn = int(read())
conn = int(read())
g = [[] for i in range(cn+1)]

for i in range(conn):
    a, b = map(int, read().split())
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(1)
dfs = []
visited = [False] * (cn+1)
visited[1] = True

while q:
    cur = q.popleft()

    for i in g[cur]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            dfs.append(i)

print(len(dfs))