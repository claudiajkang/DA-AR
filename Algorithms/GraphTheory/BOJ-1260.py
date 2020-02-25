from sys import stdin
from queue import Queue

N, M, V = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
dvisit = [False for _ in range(N + 1)]
bvisit = [False for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for _ in range(N + 1):
    graph[_].sort()

dfs_result = []


def dfs(graph, c):
    dfs_result.append(str(c))
    dvisit[c] = True
    for i in graph[c]:
        if not dvisit[i]:
            dvisit[i] = True
            dfs(graph, i)


bfs_result = []


def bfs(graph, c):
    bq = Queue()
    bq.put(c)
    bvisit[c] = True
    while len(bq.queue):
        cur = bq.get()
        bfs_result.append(str(cur))
        for i in graph[cur]:
            if not bvisit[i]:
                bvisit[i] = True
                bq.put(i)


dfs(graph, V)
bfs(graph, V)

print(' '.join(dfs_result))
print(' '.join(bfs_result))