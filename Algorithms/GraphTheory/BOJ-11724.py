from sys import stdin

N, M = map(int, stdin.readline().split())
visited = [False for i in range(N+1)]
g = [[] for i in range(N+1)]
c = 0

for i in range(M):
    A, B = map(int, stdin.readline().split())
    g[A].append(B)
    g[B].append(A)

for i in range(1, N+1):
    if not visited[i]:
        c += 1
        dstack = [i]

        while dstack:
            cur = dstack.pop()
            visited[cur] = True
            for j in sorted(g[cur]):
                if not visited[j]:
                    visited[j] = True
                    dstack.append(j)
    elif c == N:
        break

print(c)
