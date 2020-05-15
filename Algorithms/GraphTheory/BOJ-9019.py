from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    a, b = map(int, read().split())

    visited = [False] * 10000

    q = deque()
    q.append([a, ''])

    v = ['D', 'S', 'L', 'R']
    cmd = ''

    while q:
        n, cmd = q.popleft()

        if n == b:
            break

        d = 2 * n if (2 * n) <= 9999 else (2 * n) % 10000
        s = n - 1 if n > 0 else 9999
        l = (n * 10) % 10000 + (n // 1000)
        r = (n // 10) + (n % 10) * 1000

        tmp = [d, s, l, r]
        for i in range(4):
            if not visited[tmp[i]]:
                visited[tmp[i]] = True
                q.append([tmp[i], cmd + v[i]])

    print(cmd)
