from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    st = [0] + list(map(int, stdin.readline().split()))
    res = []
    visited = [False for _ in range(n + 1)]

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            dstack = [i]
            cycle = []

            while dstack:
                cur = dstack.pop()
                cycle.append(cur)

                nexts = st[cur]
                if not visited[nexts]:
                    dstack.append(nexts)
                    visited[nexts] = True
                else:
                    if nexts in cycle:
                        cdx = cycle.index(nexts)
                        res += cycle[cdx:]

    print(n - len(res))

