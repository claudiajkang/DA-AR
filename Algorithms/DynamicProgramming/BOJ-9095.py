import sys

T = int(sys.stdin.readline())
m = 12
dp = [0 for i in range(m)]

for i in range(1, m):
    if i == 1:
        dp[i] = 1
    elif i == 2: 
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    idx = int(sys.stdin.readline())
    print(dp[idx])

