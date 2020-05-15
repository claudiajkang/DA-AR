from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    mid = (lo + hi) // 2

    c = 0
    for i in range(1, n + 1):
        c += (min(i * n, mid) // i)

    if c >= k:
        return lo, mid

    else:
        return mid, hi


n = int(read())
k = int(read())

lo = 0
hi = n ** 2

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)
