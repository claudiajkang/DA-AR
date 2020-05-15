from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n] % 15746)
