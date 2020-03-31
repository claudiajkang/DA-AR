from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n = int(read())
k = int(read())
b = [[-1] + [0] * n + [-1] for i in range(n+2)]
b[0] = [-1] * (n+2)
b[-1] = [-1] * (n+2)

for i in range(k):
    x, y = map(int, read().split())
    b[x][y] = 1

time = deque()
direction = deque()
time.append(0)
direction.append(0)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

l = int(read())
for i in range(l):
    t, d = read().split()
    time.append(int(t))
    direction.append(1 if d == 'D' else -1)

snake = deque()
x, y = 1, 0
d = 0

for t in range(10101):
    x += dx[d]
    y += dy[d]

    if b[x][y] == -1:
        print(t)
        exit()

    if [x, y] in snake:
        print(t)
        exit()

    if b[x][y] != 1:
        if snake: snake.popleft()

    if b[x][y] == 1:
        b[x][y] = 0

    snake.append([x, y])

    if t in time:
        time.popleft()
        d += direction.popleft()
        if d == 4: d = 0
        elif d == -1: d = 3