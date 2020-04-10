from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
mn = 10 ** 6
pos = [-1] * (mn + 1)

if n == k:
    print(0)

else:
    q = deque()
    q.append(n)
    pos[n] = 0

    while q:
        cur = q.popleft()

        for i in [cur - 1, cur + 1, 2 * cur]:
            if 0 <= i <= mn and pos[i] == -1:
                q.append(i)
                pos[i] = pos[cur] + 1

    print(pos[k], end="")
