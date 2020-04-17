from sys import stdin

a, b, v = map(int, stdin.readline().rstrip().split())

lo = 0
hi = (v // (a - b)) + 1
res = 0

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    temp = (a - b) * mid + b

    if temp >= v:
        hi = mid
    else:
        lo = mid

print(hi)
