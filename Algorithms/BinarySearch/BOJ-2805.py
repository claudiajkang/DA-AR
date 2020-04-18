from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global m, tree, res

    mid = (lo + hi) // 2

    s = 0
    for t in tree:
        s += (t - mid) if t > mid else 0

    if s >= m:
        res = mid
        return mid + 1, hi

    else:
        return lo, mid - 1


n, m = map(int, read().split())
tree = list(map(int, read().split()))

lo = 0
hi = max(tree)
res = 0

while lo <= hi:
    lo, hi = bs(lo, hi)

print(res)
