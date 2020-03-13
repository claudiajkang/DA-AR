from sys import stdin
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())

dp = [[0] * (k+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[n][k])
