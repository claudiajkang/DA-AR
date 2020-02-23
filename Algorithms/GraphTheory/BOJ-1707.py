import sys

K = int(sys.stdin.readline())

for l in range(K):
    V, E = map(int, sys.stdin.readline().split())
    g = [[] for i in range(V + 1)]

    for i in range(E):
        A, B = map(int, sys.stdin.readline().split())
        g[A].append(B)
        g[B].append(A)

    visited = [-1 for i in range(V + 1)]
    color = 1
    res = 0

    for i in range(1, V + 1):
        if visited[i] == -1:
            dstack = [i]
            visited[i] = color

            while dstack:
                cur = dstack.pop()
                color2 = int((visited[cur] + 1) % 2)
                for j in g[cur]:
                    if visited[j] == -1:
                        visited[j] = color2
                        dstack.append(j)
                    elif visited[j] != color2:
                        res = 1
                        break
                if res:
                    break

                color = color2

    print(["YES", "NO"][res])
