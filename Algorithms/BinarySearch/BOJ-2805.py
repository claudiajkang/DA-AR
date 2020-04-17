from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
h = list(map(int, read().split()))

lo = 0
hi = max(h)

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    s = 0
    for th in h:
        s += (th - mid) if th > mid else 0

    if s >= m:
        lo = mid
    else:
        hi = mid

print(lo)
