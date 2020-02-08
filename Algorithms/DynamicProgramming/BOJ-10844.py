import sys

N = int(sys.stdin.readline())
dp = [[0 for i in range(10)] for j in range(101)]
v = 1000000000

for j in range(10):
    dp[1][j] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]

        elif j == 9:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % v


print((sum(dp[N])-dp[N][0]) % v)
