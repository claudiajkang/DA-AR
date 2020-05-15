from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))

dp1 = [0] * n
dp2 = [0] * n

for i in range(n):
    for j in range(i - 1, -1, -1):
        if a[j] < a[i]:
            dp1[i] = max(dp1[i], dp1[j])

    dp1[i] += 1

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[j] < a[i]:
            dp2[i] = max(dp2[i], dp2[j])

    dp2[i] += 1

for i in range(n):
    dp1[i] += dp2[i]

print(max(dp1) - 1)
