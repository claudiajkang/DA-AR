from sys import stdin
from heapq import heappush, heappop, nlargest
read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    m = int(read())
    arr = [0]

    for i in range(m // 10 + 1):
        arr += list(map(int, read().split()))

    l = []
    r = []
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
            if val <= r[0]:
                heappush(l, (-1)*val)
                mid = heappop(l) * (-1)

            else:
                heappush(r, val)
                mid = heappop(r)

            res.append(mid)

        else:
            if val <= mid:
                heappush(r, mid)
                mid = val
                heappush(l, (-1)*mid)

            else:
                heappush(l, (-1)*mid)
                mid = val
                heappush(r, mid)

        if len(res) == 10:
            print(' '.join(map(str, res)))
            res = []

    if res:
        print(' '.join(map(str, res)))