from sys import stdin

K = int(stdin.readline())

for l in range(K):
    V, E = map(int, stdin.readline().split())
    g = [[] for i in range(V + 1)]

    for i in range(E):
        A, B = map(int, stdin.readline().split())
        g[A].append(B)
        g[B].append(A)

    visited = [False for i in range(V + 1)]
    color = ['R', 'G']
    res = 0
    for i in range(1, V + 1):
        if not visited[i]:
            visited[i] = color[int(i % 2)]
            dstack = [i]

            while dstack:
                cur = dstack.pop()
                cdx = color.index(visited[cur])
                for j in g[cur]:
                    if not visited[j]:
                        visited[j] = color[int((cdx + 1) % 2)]
                        dstack.append(j)
                    elif visited[j] != color[int((cdx + 1) % 2)]:
                        res = 1
                        break
                if res:
                    break
    print(["YES", "NO"][res])
