from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
indegree = [0] * (n + 1)
adj = [[] for i in range(n + 1)]

for i in range(m):
    l = list(read())

    for j in range(1, l[0]):
        adj[l[j]].append(l[j + 1])
        indegree[l[j + 1]] += 1

result = [0] * (n + 1)

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

for i in range(1, n + 1):
    if not q:
        print("0")
        exit()

    cur = q.popleft()
    result[i] = cur

    for j in adj[cur]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)

for i in range(1, n + 1):
    print(result[i])
