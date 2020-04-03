from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
k = int(read())

b = [[-1] + [0] * n + [-1] for i in range(n + 2)]
b[0] = [-1] * (n + 2)
b[-1] = [-1] * (n + 2)

for i in range(k):
    x, y = map(int, read().split())
    b[x][y] = 1

l = int(read())
time = deque()
direction = deque()

time.append(0)
direction.append(0)

for i in range(l):
    t, d = read().split()
    time.append(int(t))
    direction.append(1 if d == 'D' else -1)

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
x, y = 1, 0
di = 0
snake = deque()

for t in range(10101):
    x += d[di][0]
    y += d[di][1]

    if [x, y] in snake:
        print(t)
        exit()

    if b[x][y] == -1:
        print(t)
        exit()

    if b[x][y] == 0:
        if snake: snake.popleft()

    if b[x][y] == 1:
        b[x][y] = 0

    snake.append([x, y])

    if t in time:
        time.popleft()
        di += direction.popleft()
        if di == 4: di = 0
        if di == -1: di = 3
