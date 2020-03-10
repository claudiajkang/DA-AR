from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
an = list(map(int, read().split()))
dp = [0] * (n+1)

for i in range(n):
    dp[i+1] = dp[i] + an[i]

for k in range(m):
    i, j = map(int, read().split())
    print(dp[j] - dp[i-1])
