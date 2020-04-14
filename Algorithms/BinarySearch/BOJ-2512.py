from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
lm = list(map(int, read().split()))
m = int(read())

if sum(lm) <= m:
    print(max(lm))
    exit()

lo = 0
hi = m

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    s = 0
    for i in lm:
        s += min(i, mid)

    if s <= m:
        lo = mid
    else:
        hi = mid

print(lo)
