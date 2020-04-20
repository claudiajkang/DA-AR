from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def bs(lo, hi):
    global a, b, v

    mid = (lo + hi) // 2

    t = (a - b) * mid + b

    if t >= v:
        return lo, mid

    else:
        return mid, hi


a, b, v = map(int, stdin.readline().rstrip().split())

lo = 0
hi = 10 ** 9

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)
