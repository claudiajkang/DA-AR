from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
dp = [0] * (n + 1)
pn = []

for i in range(1, n):
    if i ** 2 > n: break
    pn.append(i ** 2)
    dp[i ** 2] = 1

for i in range(1, n + 1):
    if dp[i] == 1: continue

    a = []

    for j in pn:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])

    if not a:
        dp[i] = -1

    else:
        dp[i] = min(a) + 1

print(dp[n])
