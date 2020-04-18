from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()

def bs(lo, hi):
    global m, money

    mid = (lo + hi) // 2
    c = 0
    s = 0

    for mm in money:
        if mm > mid:
            return mid, hi

        s += mm
        if s > mid:
            s = mm
            c += 1

    if s > 0:
        c += 1

    if c > m:
        return mid, hi
    else:
        return lo, mid


n, m = map(int, read().split())
money = [int(read()) for i in range(n)]
lo = 1
hi = sum(money)

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)
