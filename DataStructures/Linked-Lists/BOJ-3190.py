from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n = int(read())
board = [[-1] + [0]*n + [-1] for i in range(n+2)]
board[0] = [-1] * (n+2)
board[-1] = [-1] * (n+2)

k = int(read())

for i in range(k):
    x, y = map(int, read().split())
    board[x][y] = 1

l = int(read())
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
time = deque()
time.append(0)
direction = deque()
direction.append(d[0])
tidx = 0

for i in range(l):
    t, td = read().split()
    if td == 'D':
        tidx += 1
        if tidx == 4: tidx = 0
    elif td == 'L':
        tidx -= 1
        if tidx == -1: tidx = 3

    time.append(int(t))
    direction.append(d[tidx])

snake = deque()
x, y = 1, 1
cx, cy = 0, 0

for t in range(10101):
    x += cx
    y += cy

    if board[x][y] == -1:
        print(t)
        exit()

    if [x, y] in snake:
        print(t)
        exit()

    if board[x][y] != 1:
        if snake: snake.popleft()

    if board[x][y] == 1:
        board[x][y] = 0

    snake.append([x, y])

    if t in time:
        time.popleft()
        cx, cy = direction.popleft()