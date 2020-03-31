from sys import stdin
from heapq import heappush, heappop
read = lambda: int(stdin.readline().rstrip())

n = read()
arr = [0] * (n+1)
l = []
r = []
mid = 0
res = []

for i in range(1, n+1):
    arr[i] = read()

    if i % 2:
        if not r:
            mid = arr[i]
            heappush(r, mid)
        elif arr[i] <= r[0]:
            heappush(l, arr[i] * (-1))
            mid = heappop(l) * (-1)
            heappush(r, mid)
        else:
            heappush(r, arr[i])
            mid = heappop(r)
            heappush(r, mid)
        res.append(mid)
    else:
        if arr[i] <= mid:
            heappush(l, arr[i] * (-1))
            res.append(l[0] * (-1))
        else:
            heappush(l, heappop(r) * (-1))
            heappush(r, arr[i])
            res.append(l[0] * (-1))

print('\n'.join(map(str, res)))