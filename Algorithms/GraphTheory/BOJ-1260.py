from sys import stdin
from queue import Queue

N, M, V = map(int, stdin.readline().split())
g = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, stdin.readline().split())
    g[A].append(B)
    g[B].append(A)

dstack = [V]
dfs = []

for i in range(1, N+1):
    g[i] = sorted(g[i])

while dstack:
    cur = dstack.pop()
    if str(cur) not in dfs:
        dfs.append(str(cur))

    for i in reversed(g[cur]):
        if str(i) not in dfs:
            dstack.append(i)

vqueue = Queue()
vqueue.put(V)
vfs = []

while len(vqueue.queue):
    cur = vqueue.get()
    if str(cur) not in vfs:
        vfs.append(str(cur))

    for i in g[cur]:
        if str(i) not in vfs:
            vqueue.put(i)

print(' '.join(dfs))
print(' '.join(vfs))
