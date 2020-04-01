from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

k = int(read())

for tt in range(k):
    v, e = map(int, read().split())

    g = [[] for i in range(v+1)]

    for i in range(e):
        a, b = map(int, read().split())
        g[a].append(b)
        g[b].append(a)

    vcolor = [None] * (v+1)
    color = ['R', 'B']
    ci = True
    err = False

    for i in range(1, v+1):
        if vcolor[i] is None:
            q = deque()
            vcolor[i] = color[ci]
            q.append(i)

            while q:
                c = q.popleft()
                ci = color.index(vcolor[c])

                for j in g[c]:
                    if vcolor[j] is None:
                        q.append(j)
                        vcolor[j] = color[not ci]

                    elif vcolor[j] != color[not ci]:
                        err = True
                        break

                if err:
                    break

    print(['YES', 'NO'][err])