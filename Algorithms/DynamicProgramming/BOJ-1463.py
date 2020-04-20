from sys import stdin

x = int(stdin.readline().rstrip())
dp = [0, 0, 1, 1]
if x <= 3:
    print(dp[x])
    exit()

dp = dp + [0] * x
mn = 10 ** 6 + 1

for i in range(4, x + 1):
    t1 = dp[i - 1] + 1

    t2 = mn
    if i % 2 == 0:
        t2 = dp[i // 2] + 1

    t3 = mn
    if i % 3 == 0:
        t3 = dp[i // 3] + 1

    dp[i] = min(t1, t2, t3)

print(dp[x])
