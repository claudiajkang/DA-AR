from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
dp = [0, 1, 2] + [0] * n

if n > 2:
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
