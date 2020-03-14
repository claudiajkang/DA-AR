from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
p = [0] + list(map(int, read().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = p[i]
    for j in range(i-1, 0, -1):
        if i % j == 0:
            dp[i] = max(dp[i], (i//j)*dp[j], dp[j] + dp[i-j])
        else:
            dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[n])
