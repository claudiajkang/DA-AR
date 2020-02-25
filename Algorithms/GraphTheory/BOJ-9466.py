from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    st = [0] + list(map(int, stdin.readline().strip().split()))
    visited = [False] * (n+1)
    res = []

    for i in range(1, n+1):
        if not visited[i]:
            dstack = [i]
            cycle = []

            while dstack:
                cur = dstack.pop()
                visited[cur] = True
                nexts = st[cur]
                cycle.append(cur)

                if visited[nexts]:
                    if nexts in cycle:
                        cdx = cycle.index(nexts)
                        res += cycle[cdx:]
                        break
                else:
                    dstack.append(nexts)

    print(n-len(res))
