from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n = int(read())
RGB = [['0'] * (n+2) for i in range(n+2)]
R_B = [['0'] * (n+2) for i in range(n+2)]

for i in range(1, n+1):
    r = read()
    RGB[i] = ['0'] + list(r) + ['0']
    r = r.replace('G', 'R')
    R_B[i] = ['0'] + list(r) + ['0']

res = [0, 0]
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(1, n+1):
    for j in range(1, n+1):
        if RGB[i][j] != '0':
            q = deque()
            dfs = deque()
            color = RGB[i][j]
            RGB[i][j] = '0'

            q.append([i, j])
            dfs.append([i, j])

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    ti, tj = ci + ii, cj + jj
                    if RGB[ti][tj] == color:
                        RGB[ti][tj] = '0'
                        q.append([ti, tj])
                        dfs.append([ti, tj])

            if dfs:
                res[0] += 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if R_B[i][j] != '0':
            q = deque()
            dfs = deque()
            color = R_B[i][j]
            R_B[i][j] = '0'

            q.append([i, j])
            dfs.append([i, j])

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    ti, tj = ci + ii, cj + jj
                    if R_B[ti][tj] == color:
                        R_B[ti][tj] = '0'
                        q.append([ti, tj])
                        dfs.append([ti, tj])

            if dfs:
                res[1] += 1

print(' '.join(map(str, res)))