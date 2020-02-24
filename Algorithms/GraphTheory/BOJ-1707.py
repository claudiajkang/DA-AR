from sys import stdin

K = int(stdin.readline())

for t in range(K):
    V, E = map(int, stdin.readline().strip().split())
    g = [[] for l in range(V + 1)]

    for j in range(E):
        A, B = map(int, stdin.readline().strip().split())
        g[A].append(B)
        g[B].append(A)

    res = 0
    visited = [None for l in range(V + 1)]
    color = ['R', 'G']

    for i in range(1, V + 1):
        if not visited[i]:
            dstack = [i]
            visited[i] = color[0]

            while dstack:
                cur = dstack.pop()
                ci = color.index(visited[cur])
                tc = color[int((ci+1) % 2)]
                for j in g[cur]:
                    if not visited[j]:
                        dstack.append(j)
                        visited[j] = tc
                    elif visited[j] != tc:
                        res = 1
                        break
                if res:
                    break

    print(["YES", "NO"][res])
