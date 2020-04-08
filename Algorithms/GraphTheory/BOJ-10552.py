from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m, p = map(int, read().split())

channel = [0] * (m + 1)

for i in range(n):
    l, d = map(int, read().split())
    if channel[d] == 0:
        channel[d] = l

watched = [False] * (m + 1)
q = deque()
q.append(p)
res = 0
err = False
watched[p] = True

while q:
    cur = q.popleft()

    if not watched[channel[cur]]:
        if channel[cur] > 0:
            q.append(channel[cur])
            watched[channel[cur]] = True
            res += 1
        else:
            break
    else:
        err = True
        break

print(-1 if err else res)
