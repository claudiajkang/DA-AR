from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
b = [[] for i in range(n + 1)]
con = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    l = list(map(int, read().split()))
    time[i] = l[0]

    for j in l[1:]:
        if j != -1:
            b[j].append(i)
            con[i] += 1

q = []
restime = [0] * (n + 1)
for i in range(1, n + 1):
    if con[i] == 0:
        heappush(q, [con[i], i])
        restime[i] = time[i]

for i in range(1, n + 1):
    cons, cur = heappop(q)

    for j in b[cur]:
        con[j] -= 1
        restime[j] = max(restime[j], restime[cur] + time[j])
        if con[j] == 0:
            heappush(q, [con[i], j])

print('\n'.join(map(str, restime[1:])))
