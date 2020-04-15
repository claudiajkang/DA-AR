from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
g = [[] for i in range(n + 1)]
con = [0] * (n + 1)

for i in range(m):
    l = list(map(int, read().split()))

    for j in range(1, l[0]):
        g[l[j]].append(l[j + 1])
        con[l[j + 1]] += 1

q = deque()

for i in range(1, n + 1):
    if con[i] == 0:
        q.append(i)

result = [0] * (n + 1)
err = False

for i in range(1, n + 1):
    if not q:
        err = True
        break

    cur = q.popleft()
    result[i] = cur

    for j in g[cur]:
        con[j] -= 1
        if con[j] == 0:
            q.append(j)

if err:
    print(0)
else:
    print('\n'.join(map(str, result[1:])))
