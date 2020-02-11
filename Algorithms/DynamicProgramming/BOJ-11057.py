import sys

N = int(sys.stdin.readline())
dp = [[0 for i in range(10)] for j in range(N+1)]
v = 10007

for i in range(10):
    dp[1][i] = 1

if N >= 2:
    for i in range(10):
        dp[2][i] = (10 - i)

if N > 2:
    for i in range(3, N+1):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][j:]) % v

print(sum(dp[N])%v)
