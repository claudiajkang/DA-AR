from sys import stdin
read = lambda: stdin.readline().rstrip()

def search():
    global board, res

    for i in range(n):
        temp = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                temp += 1
            else:
                res = max(temp, res)
                temp = 1

        res = max(temp, res)

    for j in range(n):
        temp = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                temp += 1

            else:
                res = max(temp, res)
                temp = 1

        res = max(temp, res)


n = int(read())
board = [[] for i in range(n)]

for i in range(n):
    board[i] = list(read())

res = 0
flag = True
search()

for i in range(n):
    if i == (n - 1): flag = False
    for j in range(n - 1):
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        search()
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if flag:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            search()
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(res)