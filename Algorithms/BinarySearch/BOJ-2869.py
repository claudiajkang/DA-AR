from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

a, b, v = map(int, read().split())

if a == v:
    print(1)
    exit()

lo = 1
hi = 10 ** 9 + 1

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    tv = mid * (a - b) + b

    if tv >= v:
        hi = mid
    else:
        lo = mid

print(hi)