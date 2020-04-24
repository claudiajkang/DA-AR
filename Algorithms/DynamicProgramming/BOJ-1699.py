from sys import stdin

n = int(stdin.readline().rstrip())
pn = []
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i * i > n: break
    dp[i * i] = 1
    pn.append(i * i)

for i in range(1, n + 1):
    if dp[i] == 1: continue

    a = []

    for j in pn:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])

    dp[i] = min(a) + 1 if a else -1

print(dp[n])