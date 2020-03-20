from sys import stdin
from collections import deque

read = lambda: stdin.readline().rstrip()

t = int(read())

for i in range(t):
    n, m = map(int, read().split())
    doc = list(map(int, read().split()))
    q = deque()

    for i in range(n):
        q.append([doc[i], i])

    doc.sort(reverse=True)
    mi = 0
    c = 0
    while True:
        tp, ti = q.popleft()
        
        if doc[mi] > tp:
            q.append([tp, ti])
            continue
        
        else:
            mi += 1

        c += 1
        if ti == m:
            print(c)
            break

