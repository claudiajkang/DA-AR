from collections import deque
from sys import stdin

f, s, g, u, d = map(int, stdin.readline().rstrip().split())
d = d * (-1)
b = [-1] * (10 ** 6 + 1)

q = deque()
q.append(s)
b[s] = 0
done = False

while q:
    cur = q.popleft()

    if cur == g:
        done = True
        break

    for i in [u, d]:
        t = cur + i
        if (1 <= t <= f) and b[t] == -1:
            b[t] = b[cur] + 1
            q.append(t)

if done:
    print(b[g], end="")
else:
    print("use the stairs", end="")
