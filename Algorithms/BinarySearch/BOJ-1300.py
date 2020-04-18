from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def search(lo, hi):
    global n, k

    mid = (lo + hi) // 2

    c = 0
    for i in range(1, n + 1):
        c += min(mid // i, n)

    if c >= k:
        return lo, mid
    else:
        return mid, hi


n = int(read())
k = int(read())

lo = 1
hi = k

while (lo + 1) < hi:
    lo, hi = search(lo, hi)

print(hi)