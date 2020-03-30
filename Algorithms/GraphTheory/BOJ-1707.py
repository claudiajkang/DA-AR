from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

t = int(read())
result = [''] * t

for tt in range(t):
    v, e = map(int, read().split())
    g = {i : [] for i in range(1, v+1)}

    for i in range(e):
        a, b = map(int, read().split())
        g[a].append(b)
        g[b].append(a)

    visited = [False for i in range(v+1)]

    color = ['R', 'G']
    res = False

    for i in range(1, v+1):
        if not res and not visited[i]:
            cdx = int(i%2)
            visited[i] = color[cdx]
            q = deque()
            q.append([cdx, i])

            while q:
                cdx, cur = q.popleft()
                tdx = int((cdx+1) % 2)

                for k in g[cur]:
                    if not visited[k]:
                        visited[k] = color[tdx]
                        q.append([tdx, k])

                    elif visited[k] != color[tdx]:
                        res = True
                        break

                if res:
                    break

            if res:
                break

    result[tt] = ['YES', 'NO'][res]

print('\n'.join(result))