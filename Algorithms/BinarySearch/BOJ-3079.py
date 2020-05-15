from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global time, m

    mid = (lo + hi) // 2
    s = 0

    for t in time:
        s += (mid // t)

    if s >= m:
        return lo, mid

    else:
        return mid, hi


n, m = map(int, read().split())
time = [int(read()) for i in range(n)]
time.sort()

lo = 0
hi = time[-1] * m

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)
