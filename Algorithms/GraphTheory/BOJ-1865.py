from sys import stdin

read = lambda: stdin.readline().rstrip()

tc = int(read())

for ttc in range(tc):
    n, m, w = map(int, read().split())
    g = [[] for i in range(n + 1)]

    for i in range(m):
        a, b, c = map(int, read().split())
        g[a].append([b, c])
        g[b].append([a, c])

    for i in range(w):
        a, b, c = map(int, read().split())
        g[a].append([b, -c])

    INF = 1e9
    dist = [INF] * (n + 1)
    dist[1] = 0

    err = False
    for i in range(1, n + 1):
        err = False
        for j in range(1, n + 1):
            for cur, d in g[j]:
                if dist[cur] > dist[j] + d:
                    dist[cur] = dist[j] + d
                    err = True

        if not err: break

    if err:
        print("YES")
    else:
        print("NO")
