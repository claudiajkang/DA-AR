from sys import stdin
from heapq import heappush, heappop

n = int(stdin.readline().rstrip())
maxhq = []
minhq = []
res = []
mid = 0

for i in range(1, n+1):
    val = int(stdin.readline().rstrip())

    if i % 2:
        if maxhq and val < (maxhq[0] * (-1)):
            mid = heappop(maxhq) * (-1)
            heappush(maxhq, val * (-1))

        elif minhq and minhq[0] < val:
            mid = heappop(minhq)
            heappush(minhq, val)

        else:
            mid = val

        res.append(mid)

    else:
        if val < mid:
            heappush(minhq, mid)
            heappush(maxhq, val*(-1))

        else:
            heappush(maxhq, (-1) * mid)
            heappush(minhq, val)

        res.append(maxhq[0] * (-1))

print('\n'.join(map(str, res)))
