from sys import stdin

x = int(stdin.readline().rstrip())

dp = [0, 0, 1, 1] + [0] * x
INF = 10 ** 6

if x > 3:
    for i in range(4, x + 1):
        t1 = dp[i - 1] + 1
        t2 = INF
        t3 = INF

        if i % 2 == 0:
            t2 = dp[i // 2] + 1

        if i % 3 == 0:
            t3 = dp[i // 3] + 1

        dp[i] = min(t1, t2, t3)

print(dp[x])
