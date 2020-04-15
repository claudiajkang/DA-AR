from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
l = list(map(int, read().split()))
m = int(read())

lo = 0
hi = sum(l)

if hi <= m:
    print(max(l))

else:
    while (lo + 1) < hi:
        mid = (lo + hi) // 2

        s = 0
        for ll in l:
            s += min(ll, mid)

        if s <= m:
            lo = mid
        else:
            hi = mid

    print(lo)
