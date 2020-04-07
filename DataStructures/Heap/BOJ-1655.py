from heapq import heappush, heappop
from sys import stdin

read = lambda: int(stdin.readline().rstrip())

n = read()
arr = [0] + [read() for i in range(n)]
res = []
l = []
r = []

for i in range(1, n+1):
    if i % 2:
        if not r:
            heappush(r, arr[i])
        elif arr[i] <= r[0]:
            heappush(l, arr[i] * (-1))
        else:
            heappush(r, arr[i])
            heappush(l, heappop(r) * (-1))
        res.append(r[0])
    else:
        if arr[i] <= r[0]:
            heappush(l, arr[i] * (-1))
            heappush(r, heappop(l) * (-1))
        else:
            heappush(r, arr[i])
        res.append(r[0])

print('\n'.join(map(str, res)))