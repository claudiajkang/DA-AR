from sys import stdin
from heapq import heappush, heappop

t = int(stdin.readline().rstrip())

for tt in range(t):
    m = int(stdin.readline().rstrip())
    arr = [0]

    for i in range(m // 10 + 1):
        arr += list(map(int, stdin.readline().rstrip().split()))

    minhq = []
    maxhq = []
    mid = 0

    print(len(arr) // 2)
    res = []

    for i in range(1, m+1):
        val = arr[i]

        if i == 1:
            mid = val
            res.append(mid)
            continue

        elif i % 2:
            if val <= minhq[0]:
                heappush(maxhq, (-1) * val)
                mid = (-1) * heappop(maxhq)

            else:
                heappush(minhq, val)
                mid = heappop(minhq)

            res.append(mid)

        else:
            if val <= mid:
                heappush(minhq, mid)
                heappush(maxhq, (-1) * val)

            else:
                heappush(maxhq, (-1) * mid)
                heappush(minhq, val)

        if len(res) == 10:
            print(' '.join(map(str, res)))
            res = []

    if res:
        print(' '.join(map(str, res)))
