from sys import stdin

def dfs(v, g, d):
    d[v] = True
    dstack = [v]

    while dstack:
        cur = dstack.pop()
        for i in sorted(g[cur]):
            if not d[i]:
                dstack.append(i)
                d[i] = True

    return d


N, M = map(int, stdin.readline().split())
G = [[] for _ in range(N+1)]
A, B = 0, 0

for i in range(M):
    A, B = map(int, stdin.readline().split())
    G[A].append(B)
    G[B].append(A)

visited = [False for i in range(N+1)]
c = 0

for i in range(1, N+1):
    if visited[i]:
        continue
    elif c == N:
        break
    else:
        c += 1
        visited = dfs(i, G, visited)

print(c)
