from sys import stdin
read = lambda: stdin.readline().rstrip()

n = list(map(int, list(read())))
l = len(n)
dp = [0] * (l+1)

dp[0] = 1
for i in range(1, l+1):
    if 1 <= n[i-1] <= 9:
        dp[i] += dp[i-1]
    if i == 1:
        continue
    value = (n[i-2] * 10 + n[i-1])
    if 10 <= value <= 26:
        dp[i] += dp[i-2]

print(dp[l] % 1000000)