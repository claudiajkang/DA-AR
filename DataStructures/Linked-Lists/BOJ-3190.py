from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())
board = [[-1] + [0] * n + [-1] for i in range(n+2)]
board[0] = [-1] * (n+2)
board[-1] = [-1] * (n+2)
x, y = 0, 0

for i in range(k):
    x, y = map(int, stdin.readline().rstrip().split())
    board[x][y] = 1

l = int(stdin.readline().rstrip())
time = deque()
direction = deque()
time.append(0)
direction.append(0)

for i in range(l):
    x, y = stdin.readline().rstrip().split()
    time.append(int(x))

    if y == 'D':
        direction.append(1)

    elif y == 'L':
        direction.append(-1)

x, y = 1, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
snake = deque()

for t in range(10101):
    x += dx[d]
    y += dy[d]

    if board[x][y] == -1:
        print(t)
        exit()

    if [x, y] in snake:
        print(t)
        exit()

    if board[x][y] != 1:
        if snake:
            snake.popleft()

    if board[x][y] == 1:
        board[x][y] = 0

    snake.append([x, y])

    if t in time:
        time.popleft()
        d = (d+direction.popleft()) % 4
