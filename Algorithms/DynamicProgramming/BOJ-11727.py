from sys import stdin

n = int(stdin.readline().rstrip())
dp = [0, 1, 3] + [0] * (n + 1)

if n > 2:
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 2]) % 10007

print(dp[n])
