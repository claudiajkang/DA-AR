from sys import stdin

n = int(stdin.readline().rstrip())
dp = [0] + [0] * n
pn = []

for i in range(1, n + 1):
    if (i * i) > n: break
    pn.append(i * i)
    dp[i * i] = 1

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
