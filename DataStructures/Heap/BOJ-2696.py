from heapq import heappush, heappop
from sys import stdin

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
    res = []

    print(len(arr) // 2)

    for i in range(1, len(arr)):
        if i % 2:
            if not r:
                mid = arr[i]
            elif arr[i] <= r[0]:
                heappush(l, arr[i] * (-1))
                mid = heappop(l) * (-1)
            else:
                heappush(r, arr[i])
                mid = heappop(r)
            res.append(mid)
        else:
            if arr[i] <= mid:
                heappush(r, mid)
                heappush(l, arr[i] * (-1))
            else:
                heappush(l, mid * (-1))
                heappush(r, arr[i])

        if len(res) == 10:
            print(' '.join(map(str, res)))
            res = []

    if res:
        print(' '.join(map(str, res)))