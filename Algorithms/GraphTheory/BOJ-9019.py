from sys import stdin
from collections import deque

read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    a, b = map(int, read().split())

    prev = [False for i in range(10000)]
    q = deque()
    prev[a] = True
    q.append([a, ''])
    suc = False
    res = 0

    while q:
        qsize = len(q)
        for i in range(qsize):
            n, cmd = q.popleft()

            if n == b:
                suc = True
                res = cmd
                break

            d = 2 * n if (2 * n) <= 9999 else (2 * n) % 10000
            if not prev[d]:
                prev[d] = True
                q.append([d, cmd + 'D'])

            s = 9999 if n == 0 else n - 1
            if not prev[s]:
                prev[s] = True
                q.append([s, cmd + 'S'])

            l = (n % 1000) * 10 + (n // 1000)
            if not prev[l]:
                prev[l] = True
                q.append([l, cmd + 'L'])

            r = (n % 10) * 1000 + (n // 10)
            if not prev[r]:
                prev[r] = True
                q.append([r, cmd + 'R'])

        if suc: break

    print(res)
