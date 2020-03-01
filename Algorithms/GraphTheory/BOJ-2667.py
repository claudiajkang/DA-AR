from sys import stdin

N = int(stdin.readline())
MAP = [[] for i in range(N+2)]
MAP[0] = [-1] * (N+2)
MAP[-1] = [-1] * (N+2)
P = [[1, 0], [-1, 0], [0, 1], [0, -1]]
res = []
visited = [[False] * (N+2) for i in range(N+2)]

for i in range(1, N+1):
    MAP[i] = [-1] + list(map(int, list(stdin.readline().strip()))) + [-1]

for i in range(1, N+1):
    for j in range(1, N+1):
        if MAP[i][j] == 1 and not visited[i][j]:
            dfs = []
            dstack = [[i, j]]
            visited[i][j] = True

            while dstack:
                ci, cj = dstack.pop()
                dfs.append([ci, cj])

                for ii, jj in P:
                    ti = ii + ci
                    tj = jj + cj
                    if MAP[ti][tj] == 1 and not visited[ti][tj]:
                        dstack.append([ti, tj])
                        visited[ti][tj] = True

            res.append(len(dfs))

print(len(res))
for i in sorted(res):
    print(i)
