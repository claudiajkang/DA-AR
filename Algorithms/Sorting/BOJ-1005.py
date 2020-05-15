from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

t = int(read())
result = []
for tt in range(t):
    n, k = map(int, read().split())
    g = [[] for i in range(n+1)]
    con = [0] * (n+1)
    time = [0] + list(map(int, read().split()))

    for i in range(k):
        a, b = map(int, read().split())
        g[a].append(b)
        con[b] += 1

    w = int(read())

    q = []
    buildtime = [0] * (n+1)

    for i in range(1, n+1):
        if con[i] == 0:
            heappush(q, [con[i], i])
            buildtime[i] = time[i]

    suc = False
    while q:
        qlen = len(q)

        for i in range(qlen):
            ccon, cur = heappop(q)

            if cur == w:
                suc = True
                break

            for j in g[cur]:
                con[j] -= 1
                buildtime[j] = max(buildtime[j], buildtime[cur] + time[j])

                if con[j] == 0:
                    heappush(q, [con[j], j])

        if suc: break

    result.append(str(buildtime[w]))

print('\n'.join(result))