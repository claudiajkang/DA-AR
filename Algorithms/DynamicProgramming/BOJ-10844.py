from sys import stdin

N = int(stdin.readline())
dp = [[0] * 10 for _ in range(N+1)]
dp[1] = [0] + [1] * 9

if N > 1:
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1]

        for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

        dp[i][9] = dp[i-1][8]

print(sum(dp[N]) % 10**9)
