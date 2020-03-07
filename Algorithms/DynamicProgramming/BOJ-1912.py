from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split())) + [0]
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = a[i]
    else:
        dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))
