from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = int(read())

for tt in range(t):
    k, m, p = map(int, read().split())

    arr = [[] for i in range(m + 1)]
    con = [0] * (m + 1)

    for i in range(p):
        a, b = map(int, read().split())
        arr[a].append(b)
        con[b] += 1

    q = []
    res = [0] * (m + 1)

    for i in range(1, m + 1):
        if con[i] == 0:
            res[i] = 1
            heappush(q, [res[i], i])

    count = [0] * (m + 1)

    for i in range(1, m + 1):
        if not q: break

        ci, cur = heappop(q)

        for j in arr[cur]:
            con[j] -= 1

            if res[cur] > res[j]:
                res[j] = res[cur]
                count[j] = 1

            elif res[cur] == res[j]:
                count[j] += 1

            if con[j] == 0:
                res[j] += 1 if count[j] > 1 else 0
                heappush(q, [res[j], j])

    print(f"{k} {max(res)}")