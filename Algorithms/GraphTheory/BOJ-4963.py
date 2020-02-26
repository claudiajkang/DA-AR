from sys import stdin

for l in stdin:
    w, h = map(int, l.split())
    Point = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    if w == 0 and h == 0:
        break

    MAP = [[] for j in range(h + 2)]
    visited = [[False] * (w + 2) for i in range(h + 2)]
    MAP[0] = [0] * (w + 2)
    MAP[-1] = [0] * (w + 2)

    for m in range(h):
        MAP[m + 1] = [0] + list(map(int, stdin.readline().strip().split())) + [0]

    res = 0

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if not visited[i][j] and MAP[i][j]:
                dstack = [[i, j]]
                dfs = []

                while dstack:
                    ii, jj = dstack.pop()
                    visited[ii][jj] = True

                    if [ii, jj] not in dfs:
                        dfs.append([ii, jj])

                    for ci, cj in Point:
                        ti, tj = ci + ii, cj + jj
                        if not visited[ti][tj] and MAP[ti][tj]:
                            dstack.append([ti, tj])
                            visited[ti][tj] = True

                if dfs:
                    res += 1

    print(res)