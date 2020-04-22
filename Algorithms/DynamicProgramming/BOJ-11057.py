from sys import stdin

n = int(stdin.readline().rstrip())
dp = [[0] * 10 for i in range(n+1)]

dp[1] = [1] * 10

if n == 1:
    print(sum(dp[1]))
    exit()

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0]

    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[n])% 10007)