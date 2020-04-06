from heapq import heappush, heappop
from sys import stdin

read = lambda: int(stdin.readline().rstrip())

n = int(read())
arr = [0] + [read() for i in range(n)]
l = []
r = []
mid = []
res = []

for i in range(1, n+1):
    if i % 2:
        if not r:
            heappush(r, arr[i])
        elif arr[i] <= r[0]:
            heappush(l, arr[i] * (-1))
            heappush(r, heappop(l) * (-1))
        else:
            heappush(r, arr[i])
        mid = r[0]

    else:
        if arr[i] <= mid:
            heappush(l, arr[i] * (-1))
        else:
            heappush(r, arr[i])
            heappush(l, (-1) * heappop(r))
        mid = l[0] * (-1)

    res.append(mid)

print('\n'.join(map(str, res)))