from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global money, m

    mid = (lo + hi) // 2

    s = 0
    c = 0

    for t in money:
        if t > mid:
            return mid, hi

        if (s + t) <= mid:
            s += t
        else:
            s = t
            c += 1

    if s > 0:
        c += 1

    if c > m:
        return mid, hi
    else:
        return lo, mid


n, m = map(int, read().split())
money = [int(read()) for i in range(n)]

lo = 0
hi = sum(money)

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)
