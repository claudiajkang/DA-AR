from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
b4 = [0] * n
af = [0] * n
dp = [0] * n

for i in range(n):
    for j in range(i-1, -1, -1):
        if a[i] > a[j]:
            b4[i] = max(b4[i], b4[j])
    b4[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            af[i] = max(af[i], af[j])

    af[i] += 1
    dp[i] = b4[i] + af[i] - 1

print(max(dp))
