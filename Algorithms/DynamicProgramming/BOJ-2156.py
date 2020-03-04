from sys import stdin
read = lambda : int(stdin.readline())

n = read()
g = [0 for _ in range(n+1)]

for i in range(1, n+1):
    g[i] = read()

if 1 <= n <= 10000:
    dp = [0 for _ in range(10001)]
    dp[1] = g[1]
    for i in range(2, n+1):
        if i == 2:
            dp[2] = max(dp[1] + g[2], g[2])
        else:
            dp[i] = max(dp[i-1], g[i] + dp[i-2], g[i] + g[i-1] + dp[i-3])

    print(dp[n])

else:
    print(0)