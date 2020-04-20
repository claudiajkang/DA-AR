from sys import stdin

n = int(stdin.readline().rstrip())
dp = [0, 1, 1]

if n <= 2:
    print(dp[n])
    exit()

dp = dp + [0] * n

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])