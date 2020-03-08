from sys import stdin
read = lambda: stdin.readline().rstrip()

N, M = map(int, read().split())
T = list(map(int, read().split()))
T.sort(reverse=True)

lo = 0
hi = max(T)
mid = 0

while lo < hi:
    mid = (lo + hi) // 2
    s = 0
    for i in T:
        if i > mid:
            s += (i-mid)
        else:
            break
    if s < M:
        hi = mid
    elif s == M or lo == mid:
        break
    else:
        lo = mid

print(mid)
