from collections import deque
from sys import stdin

read = lambda: stdin.readline()

n, m, p = map(int, read().split())
channel = [-1] * (m + 1)
watched = [False] * (m + 1)

for i in range(n):
    a, b = map(int, read().split())
    if channel[b] == -1: channel[b] = a

q = deque()
q.append(p)
watched[p] = True
res = 0
dfs = []

while q:
    cur = q.popleft()
    if not watched[channel[cur]] and channel[cur] != -1:
        q.append(channel[cur])
        watched[channel[cur]] = True
        res += 1
        dfs.append(channel[cur])

    elif channel[cur] == -1:
        break

    elif watched[channel[cur]]:
        res = -1
        break

print(res)
