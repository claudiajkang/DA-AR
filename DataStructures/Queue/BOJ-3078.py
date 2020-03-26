from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
name = [deque() for i in range(21)]
res = 0

for i in range(n):
    t = len(read())
    while name[t] and name[t][0] < (i-k):
        name[t].popleft()
    res += len(name[t])
    name[t].append(i)

print(res)