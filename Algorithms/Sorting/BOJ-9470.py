from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    k, m, p = map(int, read().split())

    g = [[] for i in range(m + 1)]
    con = [0] * (m + 1)
    con2 = [0] * (m + 1)

    for i in range(p):
        a, b = map(int, read().split())
        g[a].append(b)
        con[b] += 1

    q = []
    res = [0] * (m + 1)
    visited = [False] * (m + 1)

    for i in range(1, m + 1):
        if con[i] == 0:
            heappush(q, [con[i], i])
            res[i] = 1
            visited[i] = True

    while q:
        qlen = len(q)

        for i in range(qlen):
            tcon, cur = heappop(q)

            for j in g[cur]:
                con[j] -= 1

                if res[cur] > res[j]:
                    con2[j] = 1
                    res[j] = res[cur]
                elif res[cur] == res[j]:
                    con2[j] += 1

                if con[j] == 0 and not visited[j]:
                    visited[j] = True
                    if con2[j] >= 2: res[j] += 1
                    heappush(q, [con[j], j])

    print(f"{k} {max(res)}")
