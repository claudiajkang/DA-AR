from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
up = [0] * n
do = [0] * n
dp = [0] * n

for i in range(n):
    for j in range(i-1, -1, -1):
        if a[j] < a[i]:
            up[i] = max(up[j], up[i])

    up[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[j] < a[i]:
            do[i] = max(do[i], do[j])

    do[i] += 1

    dp[i] = up[i] + do[i] - 1


print(max(dp))
