from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global m, time, res

    mid = (lo + hi) // 2

    c = 0

    for t in time:
        c += (mid // t)

    if c >= m:
        res = mid
        return lo, mid - 1
    else:
        return mid + 1, hi


n, m = map(int, read().split())
time = [int(read()) for i in range(n)]
time.sort()

lo = time[0]
hi = time[-1] * m
res = 0

while lo <= hi:
    lo, hi = bs(lo, hi)

print(res)
