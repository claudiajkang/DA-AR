from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
height = list(map(int, stdin.readline().rstrip().split()))

lo = 0
hi = max(height)

while (lo + 1) < hi:
    mid = (lo + hi) // 2
    s = 0

    for i in range(n):
        if height[i] <= mid:
            continue
        s += height[i] - mid

    if s >= m:
        lo = mid
    else:
        hi = mid

print(lo)
