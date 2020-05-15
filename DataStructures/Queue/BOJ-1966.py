from sys import stdin
from collections import deque

read = lambda: stdin.readline().rstrip()

t = int(read())

for _ in range(t):
    n, m = map(int, read().split())

    docp = list(map(int, read().split()))

    pq = deque()

    for i in range(n):
        pq.append([docp[i], i])

    c = 0
    docp.sort(reverse=True)
    mi = 0
    while True:
        v, idx = pq.popleft()
        if v == docp[mi]:
            c += 1
            mi += 1
            if idx == m:
                break
            continue
        else:
            pq.append([v, idx])

    print(c)
