from collections import deque
from sys import stdin

F, S, G, U, D = map(int, stdin.readline().rstrip().split())
D = (-1) * D
visited = [-1] * (F + 1)

if S == G:
    print(0)
    exit()

q = deque()
q.append(S)
bfs = [S]
visited[S] = 0

while q:
    cur = q.popleft()

    for i in [U, D]:
        t = cur + i

        if 1 <= t <= F:
            if visited[t] == -1:
                q.append(t)
                visited[t] = visited[cur] + 1
                bfs.append(t)
                if t == G:
                    break

    if visited[G] != -1:
        break

print(visited[G] if G in bfs else "use the stairs")
