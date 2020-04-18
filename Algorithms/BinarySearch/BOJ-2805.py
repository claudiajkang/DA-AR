from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global tree, m

    mid = (lo + hi) // 2

    s = 0

    for h in tree:
        s += 0 if h <= mid else (h - mid)

    if s >= m:
        return mid, hi

    else:
        return lo, mid

n, m = map(int, read().split())
tree = list(map(int, read().split()))

lo = 0
hi = max(tree)

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(lo)
