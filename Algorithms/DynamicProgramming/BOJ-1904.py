from sys import stdin

n = int(stdin.readline().rstrip())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i in [1, 2]:
        dp[i] = i
        continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
