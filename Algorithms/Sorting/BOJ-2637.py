from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())

arr = [[] for i in range(n + 1)]
con = [0] * (n + 1)

for i in range(m):
    x, y, k = map(int, read().split())

    arr[y].append([x, k])
    con[x] += 1

q = []
res = [[0] * (n + 1) for i in range(n + 1)]
must = []

for i in range(1, n + 1):
    if con[i] == 0:
        must.append(i)
        res[i][i] = 1
        heappush(q, i)

while q:
    cur = heappop(q)

    for j in arr[cur]:
        mid = j[0]
        count = j[1]

        for i in must:
            res[mid][i] += res[cur][i] * count

        con[mid] -= 1

        if con[mid] == 0:
            heappush(q, mid)

for i in must:
    print(f"{i} {res[n][i]}")
