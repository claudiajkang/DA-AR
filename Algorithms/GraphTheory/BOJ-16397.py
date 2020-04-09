from collections import deque
from sys import stdin

N, T, G = map(int, stdin.readline().rstrip().split())

visited = [-1] * (10 ** 6 + 1)
q = deque()
q.append(N)
visited[N] = 0
suc = False

while q:
    ci = q.popleft()

    if visited[ci] > T: break

    if ci == G:
        suc = True
        print(visited[G])
        break

    tp = [ci + 1, ci * 2]
    for i in range(2):
        nx = tp[i]
        if nx > 99999: continue
        if i and ci:
            nx -= 10 ** (len(str(nx)) - 1)
        if visited[nx] == -1:
            q.append(nx)
            visited[nx] = visited[ci] + 1

if not suc:
    print('ANG')
