from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
p = [0] + list(map(int, read().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    a = []

    for j in range(1, n+1):
        if j <= i and dp[i-j] != -1:
            a.append(p[j] + dp[i-j])

    dp[i] = max(a)

print(dp[n])