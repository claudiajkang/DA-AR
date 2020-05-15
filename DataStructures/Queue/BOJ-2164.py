from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
q = deque()

for i in range(1, n+1):
    q.append(i)

v = 0
while q:
    v = q.popleft()
    if q:
        q.append(q.popleft())

print(v)
