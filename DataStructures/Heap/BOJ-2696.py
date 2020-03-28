from sys import stdin
from heapq import heappush, heappop
from collections import deque
read = lambda: stdin.readline().rstrip()

t = int(read())

for _ in range(t):
    m = int(read())
    arr = [0]

    for j in range(m//10 + 1):
        arr += list(map(int, read().split()))

    hq = []
    res = []
    print(len(arr)//2)
    for i in range(1, m+1):
        heappush(hq, arr[i])

        if i == 1:
            res.append(arr[i])
            continue

        elif i % 2:
            idx = len(hq) // 2
            t = deque()
            for j in range(idx):
                t.append(heappop(hq))

            res.append(heappop(hq))
            heappush(hq, res[-1])

            while t:
                heappush(hq, t.popleft())

        if len(res) == 10:
            print(' '.join(map(str, res)))
            res = []

    if len(res) > 0:
        print(' '.join(map(str, res)))