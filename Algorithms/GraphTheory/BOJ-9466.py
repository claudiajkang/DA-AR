from sys import stdin

T = int(stdin.readline())

for l in stdin:
    st = [0] + list(map(int, stdin.readline().split()))
    visited = [False] * (int(l)+1)
    team = []

    for i in range(1, int(l)+1):
        if not visited[i]:
            dstack = [i]
            cycle = []
            visited[i] = True

            while dstack:
                cur = dstack.pop()
                cycle.append(cur)
                nexts = st[cur]

                if visited[nexts]:
                    if nexts in cycle:
                        cidx = cycle.index(nexts)
                        team += cycle[cidx:]
                else:
                    dstack.append(nexts)
                    visited[nexts] = True

    print(int(l) - len(team))

