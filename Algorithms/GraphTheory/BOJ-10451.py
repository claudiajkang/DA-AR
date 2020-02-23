import sys

T = int(sys.stdin.readline())

for ti in range(T):
    L = int(sys.stdin.readline())
    val = list(map(int, sys.stdin.readline().strip().split()))
    g = [[] for i in range(L+1)]

    for i in range(1, L+1):
        v = val[i-1]
        g[i].append(v)
        g[v].append(i)

    visited = [0 for i in range(L+1)]
    res = 0
    for i in range(1, L+1):
        if visited[i] == 0:
            visited[i] = 1
            dstack = [i]
            res += 1

            while dstack:
                cur = dstack.pop()
                for j in g[cur]:
                    if visited[j] == 0:
                        visited[j] = 1
                        dstack.append(j)

    print(res)
