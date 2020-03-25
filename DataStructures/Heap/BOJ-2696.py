from sys import stdin
from heapq import heappush, heappop
from collections import deque
read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    m = int(read())
    arr = [0]

    for k in range(m // 10 + 1):
        arr += list(map(int, read().split()))

    hq = []
    c = m // 2 + 1 if m % 2 else m // 2
    print(c)
    res = ""

    for i in range(1, m+1):
        heappush(hq, arr[i])

        if i == 1:
            res += str(arr[i]) + " "
            continue

        if i % 2 == 1:
            tq = deque()

            for k in range(i // 2):
                tq.append(heappop(hq))

            res += str(hq[0]) + " "

            while hq and tq:
                heappush(hq, tq.pop())

        if i == 20:
            print(res[:-1])
            res = ""

    if res != "":
        print(res)