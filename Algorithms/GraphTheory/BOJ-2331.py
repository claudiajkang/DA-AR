from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

a, p = map(int, read().split())
q = deque()
q.append(int(a))
c = 0

while True:
    t = q.pop()
    q.append(t)
    c = 0
    for i in map(int, list(str(t))):
        c += (i**p)

    if c in q:
        break

    q.append(c)

print(q.index(c))