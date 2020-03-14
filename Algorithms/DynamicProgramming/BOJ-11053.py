from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
arr = list(map(int, read().split()))
dp = [0] * n

for i in range(n):
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j])

    dp[i] += 1

print(max(dp))
