from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
name = [deque() for i in range(21)]
res = 0

for i in range(n):
    c = len(read())
    while name[c] and name[c][0] < (i-k):
        name[c].popleft()

    res += len(name[c])
    name[c].append(i)

print(res)