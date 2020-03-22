from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().rstrip().split())
q = [deque() for i in range(21)]
res = 0

for i in range(n):
    l = len(stdin.readline().rstrip())
    while q[l] and q[l][0] < (i-k):
        q[l].popleft()
    res += len(q[l])
    q[l].append(i)

print(res)
