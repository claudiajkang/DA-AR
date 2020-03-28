from sys import stdin
from heapq import heappush, heappop
read = lambda: int(stdin.readline().rstrip())

n = read()
l = []
r = []
res = []
mid = 0

for i in range(n):
    m = read()

    if i % 2:
        if mid > m:
            heappush(r, mid)
            heappush(l, m*(-1))

        else:
            heappush(l, (-1)*mid)
            heappush(r, m)

        res.append(l[0] * (-1))

    else:
        if l and (l[0] * (-1)) > m:
            mid = heappop(l) * (-1)
            heappush(l, m * (-1))

        elif r and r[0] < m:
            mid = heappop(r)
            heappush(r, m)

        else:
            mid = m

        res.append(mid)

print('\n'.join(map(str, res)))
