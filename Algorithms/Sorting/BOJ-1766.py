from heapq import heappush, heappop
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
prob = [[] for i in range(n + 1)]
con = [0] * (n + 1)

for i in range(m):
    a, b = read()
    prob[b].append(a)
    prob[a].append(b)
    con[b] += 1

q = []
result = [0] * (n + 1)

for i in range(1, n + 1):
    if con[i] == 0:
        heappush(q, i)

for i in range(1, n + 1):
    if not q: break

    cur = heappop(q)
    result[i] = cur

    for j in prob[cur]:
        con[j] -= 1
        if con[j] == 0:
            heappush(q, j)

print(' '.join(map(str, result[1:])))