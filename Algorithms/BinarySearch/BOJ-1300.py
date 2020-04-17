from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
k = int(read())

lo = 1
hi = k

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)

    if count >= k:
        hi = mid
    else:
        lo = mid

print(hi)
