from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
dp = [0] * n

for i in range(n):
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[j], dp[i])

    dp[i] += a[i]

print(max(dp))