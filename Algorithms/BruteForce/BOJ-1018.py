from sys import stdin

read = lambda: stdin.readline().rstrip()

h, w = map(int, read().split())
board = [list(read()) for i in range(h)]
res = 64

for i in range(h - 7):
    for j in range(w - 7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == s % 2:
                    if board[k][s] == 'B':
                        cnt1 += 1
                else:
                    if board[k][s] == 'W':
                        cnt1 += 1

        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == s % 2:
                    if board[k][s] == 'W':
                        cnt2 += 1
                else:
                    if board[k][s] == 'B':
                        cnt2 += 1

        res = min(res, cnt1, cnt2)

print(res)
