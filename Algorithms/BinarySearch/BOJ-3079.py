from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
time = [int(read()) for i in range(n)]

if m == 1:
    print(min(time))
    exit()

lo = 1
hi = min(time) * m + 1

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    count = 0
    for t in time:
        count += (mid // t)

    if count < m:
        lo = mid

    else:
        hi = mid

print(hi)
