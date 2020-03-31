from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    m = int(read())
    arr = [0]

    for i in range(m//10 + 1):
        arr += list(map(int, read().split()))

    print(len(arr)//2)
    res = []

    l = []
    r = []
    mid = 0

    for i in range(1, len(arr)):
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

            else:
                heappush(l, heappop(r) * (-1))
                heappush(r, arr[i])

        if len(res) == 10:
            print(' '.join(map(str, res)))
            res = []

    if res:
        print(' '.join(map(str, res)))
