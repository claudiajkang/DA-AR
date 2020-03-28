from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
name = [deque() for i in range(21)]
res = 0

for i in range(n):
    l = len(read())
    while name[l] and name[l][0] < (i-k):
        name[l].popleft()

    res += len(name[l])
    name[l].append(i)

print(res)