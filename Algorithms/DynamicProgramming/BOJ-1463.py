import sys

N = int(sys.stdin.readline())
m = 1000001
dp = [-1 for i in range(m)]

for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
    elif i in [2, 3]:
        dp[i] = 1
    else:
        dp3, dp2, dp1 = m, m, m
        if i % 3 == 0:
            dp3 = dp[int(i/3)] + 1
        if i % 2 == 0:
            dp2 = dp[int(i/2)] + 1
        dp1 = dp[i-1] + 1

        dp[i] = min(dp1, dp2, dp3)

print(dp[N])
