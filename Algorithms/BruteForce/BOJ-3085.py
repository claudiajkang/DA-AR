from sys import stdin

read = lambda: stdin.readline().rstrip()


def get_count():
    global board, res

    for i in range(n):
        temp = 1
        for j in range(1, n):
            if board[i][j - 1] == board[i][j]:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1

        res = max(res, temp)

    for i in range(n):
        temp = 1
        for j in range(n - 1):
            if board[j + 1][i] == board[j][i]:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1

        res = max(res, temp)


n = int(read())
board = [[] for i in range(n)]

for i in range(n):
    board[i] = list(read())

res = 0
flag = True

for i in range(n):
    if i == (n - 1): flag = False
    for j in range(n - 1):
        get_count()

        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        get_count()
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if flag:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            get_count()
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(res)
