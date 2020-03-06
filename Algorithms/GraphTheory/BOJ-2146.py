from sys import stdin
from collections import deque
read = lambda : stdin.readline().rstrip()

N = int(read())
M = [[-1] * (N+2) for _ in range(N+2)]
L = [[0] * (N+2) for _ in range(N+2)]
P = [[0, -1], [0, 1], [-1, 0], [1, 0]]
B = deque()

for i in range(1, N+1):
    M[i] = [-1] + list(map(int, read().split())) + [-1]
    for j in range(1, N+1):
        if [M[i][j-1], M[i][j]] == [0, 1]:
            B.append([i, j])
        elif [M[i][j], M[i][j+1]] == [1, 0]:
            B.append([i, j])

ln = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if M[i][j] == 1 and L[i][j] == 0:
            ln += 1
            L[i][j] = ln
            q = deque()
            q.append([i, j])

            while len(q):
                ci, cj = q.popleft()

                for ii, jj in P:
                    ti = ci + ii
                    tj = cj + jj
                    if M[ti][tj] == 1 and L[ti][tj] == 0:
                        L[ti][tj] = ln
                        q.append([ti, tj])

LB = [[] for _ in range(ln + 1)]
R = [10000 for _ in range(ln + 1)]

for ii, jj in B:
    LB[L[ii][jj]].append([ii, jj])

for i in range(1, ln+1):
    D = [[0] * (N+2) for _ in range(N+2)]
    q = deque()

    for ti, tj in LB[i]:
        q.append([ti, tj, 0])

    while len(q):
        ci, cj, cd = q.popleft()

        for ii, jj in P:
            ti = ci + ii
            tj = cj + jj
            if M[ti][tj] == 0 and D[ti][tj] == 0:
                D[ti][tj] = cd + 1
                q.append([ti, tj, cd + 1])

            elif M[ti][tj] == 1 and L[ti][tj] != i:
                R[i] = cd

        if R[i] != 10000:
            break

print(min(R))
