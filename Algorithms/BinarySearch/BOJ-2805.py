from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
t = list(map(int, read().split()))
t.sort(reverse=True)

lo = 0
hi = max(t)
mid = 0

while lo < hi:
    mid = (lo + hi) // 2

    s = 0
    for i in t:
        if i > mid:
            s += (i - mid)
        else:
            break

    if s < m:
        hi = mid

    elif s == m or lo == mid:
        break

    else:
        lo = mid

print(mid)
