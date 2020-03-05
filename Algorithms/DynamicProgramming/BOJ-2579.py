from sys import stdin

read = lambda: int(stdin.readline())

n = read()
s = [0 for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i] = read()

if 1 <= n <= 300:
    dp[1] = s[1]

    for i in range(2, n + 1):
        if i == 2:
            dp[i] = max(dp[i - 1] + s[i], s[i])
        else:
            dp[i] = max(s[i] + s[i - 1] + dp[i - 3], s[i] + dp[i - 2])

    print(dp[n])

else:
    print(0)
