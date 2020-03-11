from sys import stdin

n = int(stdin.readline().rstrip())

dp = [1] + [0] * n

for i in range(1, n+1):
    if i % 2 == 1:
        continue

    if i == 2:
        dp[i] = 3
        continue

    dp[i] += dp[i-2] * dp[2]
    for j in range(i-3):
        dp[i] += dp[j] * 2

print(dp[n])
