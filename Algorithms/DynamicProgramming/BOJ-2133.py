from sys import stdin

n = int(stdin.readline())
dp = [1] + [0] * n

if n < 2:
    print(0)
    exit()

dp[2] = 3
for i in range(3, n+1):
    if i % 2 == 1:
        continue
    dp[i] += dp[i-2] * dp[2]
    for j in range(0, i-3):
        dp[i] += dp[j] * 2

print(dp[n])
