from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

r, c = map(int, read().split())
m = [[] for i in range(r)]
visited = [[False] * c for i in range(r)]
p = [[-1, 0], [1, 0], [0, -1], [0, 1]]
d = [0, 0]
w = deque()
s = deque()

for i in range(r):
    m[i] = list(read())

    for j in range(c):
        if m[i][j] == 'D':
            d = [i, j]

        elif m[i][j] == 'S':
            s.append([i, j])
            visited[i][j] = True
            m[i][j] = '.'

        elif m[i][j] == '*':
            w.append([i, j])

suc = False
res = 0

while s:
    res += 1

    qsize = len(s)
    for i in range(qsize):
        si, sj = s.popleft()

        if m[si][sj] == '*': continue

        for ii, jj in p:
            ti, tj = si + ii, sj + jj

            if ti < 0 or ti >= r or tj < 0 or tj >= c:
                continue

            if m[ti][tj] == '.' and not visited[ti][tj]:
                visited[ti][tj] = True
                m[ti][tj] = '..'
                s.append([ti, tj])

            if [ti, tj] == d:
                suc = True
                break

        if suc:
            break
    if suc:
        break

    qsize = len(w)
    for i in range(qsize):
        wi, wj = w.popleft()

        for ii, jj in p:
            ti, tj = wi + ii, wj + jj

            if ti < 0 or ti >= r or tj < 0 or tj >= c:
                continue

            if '.' in m[ti][tj]:
                m[ti][tj] = '*'
                w.append([ti, tj])

print(res if suc else "KAKTUS")
