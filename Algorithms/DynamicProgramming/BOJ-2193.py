import sys

N = int(sys.stdin.readline())

dp = [0 for i in range(91)]

for i in range(1, 91):
    if i == 1 or i == 2:
        dp[i] = 1
    elif i == 3:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
