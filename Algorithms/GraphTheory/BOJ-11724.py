from sys import stdin

N, M = map(int, stdin.readline().split())
g = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, stdin.readline().split())
    g[A].append(B)
    g[B].append(A)

res = 0
visited = [False for i in range(N+1)]

for i in range(1, N+1):
    if not visited[i]:
        res += 1
        visited[i] = True

        dstack = [i]

        while dstack:
            cur = dstack.pop()
            for j in g[cur]:
                if not visited[j]:
                    visited[j] = True
                    dstack.append(j)

print(res)
