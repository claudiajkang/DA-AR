from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global money, m, res

    mid = (lo + hi) // 2

    s = 0
    c = 0
    for mm in money:
        if (s + mm) <= mid:
            s += mm
        else:
            s = mm
            c += 1

    if s > 0:
        c += 1

    if c <= m:
        res = mid
        return lo, mid - 1

    else:
        return mid + 1, hi


n, m = map(int, read().split())
money = [int(read()) for i in range(n)]

lo = max(money)
hi = sum(money)
res = 0

while lo <= hi:
    lo, hi = bs(lo, hi)

print(res)
