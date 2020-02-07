import sys

N = int(sys.stdin.readline())
m = 1001
dp = [0 for i in range(m)]

for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 3
    elif i == 4:
        dp[i] = 5
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 10007)
