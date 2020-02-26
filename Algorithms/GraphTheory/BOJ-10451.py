from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    graph = [0] + list(map(int, stdin.readline().strip().split()))
    visited = [False] * (N + 1)
    res = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dstack = [i]
            cycle = []

            while dstack:
                cur = dstack.pop()
                visited[cur] = True
                cycle.append(cur)
                nexts = graph[cur]

                if visited[nexts] and nexts in cycle:
                    res += 1
                    break
                else:
                    dstack.append(nexts)

    print(res)
