from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
dp = [a[0]] + [0] * (n-1)

for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

print(dp)
