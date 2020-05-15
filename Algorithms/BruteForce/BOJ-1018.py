from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
board = [list(read()) for i in range(n)]
res = 64

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0

        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == s % 2 and board[k][s] == 'B':
                    cnt1 += 1

                elif k % 2 != s % 2 and board[k][s] == 'W':
                    cnt1 += 1

        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if k % 2 == s % 2 and board[k][s] == 'W':
                    cnt2 += 1

                elif k % 2 != s % 2 and board[k][s] == 'B':
                    cnt2 += 1

        res = min(res, cnt1, cnt2)

print(res)