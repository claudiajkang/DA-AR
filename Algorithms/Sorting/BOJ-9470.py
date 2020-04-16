from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())
for tt in range(t):
    k, m, p = map(int, read().split())
    g = [[] for i in range(m + 1)]
    con = [0] * (m + 1)

    for i in range(p):
        a, b = map(int, read().split())
        g[a].append(b)
        con[b] += 1

    res = [0] * (m + 1)
    rcon = [0] * (m + 1)
    q = []

    for i in range(1, m + 1):
        if con[i] == 0:
            res[i] = 1
            heappush(q, [res[i], i])

    for i in range(1, m + 1):
        if not q: break

        co, cur = heappop(q)

        for j in g[cur]:
            con[j] -= 1

            if res[cur] > res[j]:
                res[j] = res[cur]
                rcon[j] = 1

            elif res[cur] == res[j]:
                rcon[j] += 1

            if con[j] == 0:
                if rcon[j] > 1:
                    res[j] += 1

                heappush(q, [res[j], j])

    print(f"{k} {max(res)}")