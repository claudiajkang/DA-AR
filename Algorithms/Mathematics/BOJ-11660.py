from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
arr = [[0] * (n+1)] + [[0] + list(map(int, read().split())) for _ in range(1, n+1)]
dp = [[0] * (n+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = dp[i][j-1] + arr[i][j]

    if i > 1:
        for j in range(1, n+1):
            dp[i][j] = dp[i][j] + dp[i-1][j]

for j in range(m):
    x1, y1, x2, y2 = map(int, read().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

