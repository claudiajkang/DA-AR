from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    a, b = map(int, read().split())
    visited = [False] * 10000

    q = deque()
    q.append([a, ''])
    cmd = ''
    suc = False

    while q:
        qsize = len(q)

        for i in range(qsize):
            cur, cmd = q.popleft()

            if cur == b:
                suc = True
                break

            d = (cur * 2) if (cur * 2) <= 9999 else (cur * 2) % 10000
            if not visited[d]:
                q.append([d, cmd + 'D'])
                visited[d] = True

            s = (cur - 1) if cur > 0 else 9999
            if not visited[s]:
                q.append([s, cmd + 'S'])
                visited[s] = True

            l = (cur * 10) % 10000 + (cur * 10) // 10000
            if not visited[l]:
                q.append([l, cmd + 'L'])
                visited[l] = True

            r = (cur // 10) + (cur % 10) * 1000
            if not visited[r]:
                q.append([r, cmd + 'R'])
                visited[r] = True

        if suc: break

    print(cmd)
