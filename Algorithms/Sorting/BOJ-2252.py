from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
g = [[] for i in range(n + 1)]
con = [0] * (n + 1)

for i in range(m):
    a, b = read()
    g[b].append(a)
    g[a].append(b)
    con[b] += 1

q = deque()
result = [0] * (n + 1)

for i in range(1, n + 1):
    if con[i] == 0:
        q.append(i)

for i in range(1, n + 1):
    if not q:
        print('0')
        break

    cur = q.popleft()
    result[i] = cur

    for j in g[cur]:
        con[j] -= 1
        if con[j] == 0:
            q.append(j)

print(' '.join(map(str, result[1:])))