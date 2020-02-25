from sys import stdin

N = int(stdin.readline())
MAP = [[] for i in range(N+2)]
visited = [[False for _ in range(N+2)] for k in range(N+1)]
res = []
Point = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(0, N+2):
    if i == 0 or i == N+1:
        MAP[i] = ['0'] * (N+2)
    else:
        MAP[i] = ['0'] + list(stdin.readline().strip()) + ['0']

for i in range(1, N+1):
    for j in range(1, N+1):
        if int(MAP[i][j]) and not visited[i][j]:
            dstack = [[i, j]]
            dfs = []

            while dstack:
                ii, jj = dstack.pop()
                visited[ii][jj] = True

                if [ii, jj] not in dfs:
                    dfs.append([ii, jj])

                for ti, tj in Point:
                    ci = ti + ii
                    cj = tj + jj
                    if int(MAP[ci][cj]) and not visited[ci][cj]:
                        dstack.append([ci, cj])
                        visited[ci][cj] = True

            res.append(len(dfs))


print(len(res))

for i in sorted(res):
    print(i)
