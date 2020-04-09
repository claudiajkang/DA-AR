from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())

if n == k:
    print(0)
    exit()

pos = [-1] * (10 ** 6 + 1)
q = deque()
q.append(n)
pos[n] = 0

while q:
    cur = q.popleft()
    if cur == k:
        break

    for ti in [cur - 1, cur + 1, cur * 2]:
        if (0 <= ti <= 10 ** 6) and pos[ti] == -1:
            pos[ti] = pos[cur] + 1
            q.append(ti)

print(pos[k])
