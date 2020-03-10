from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
un = []
dp = [0] * (n+1)

for i in range(1, n+1):
    if i*i > n:
        break
    un.append(i*i)
    dp[i*i] = 1

un.sort()

for i in range(1, n+1):
    if not dp[i]:
        dp[i] = dp[i-1] + 1
        for j in un:
            if i < j:
                break
            if dp[j] + dp[i-j] < dp[i]:
                dp[i] = dp[j] + dp[i-j]

print(dp[n])
