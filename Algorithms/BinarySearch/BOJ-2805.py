from sys import stdin, setrecursionlimit

setrecursionlimit(10 * 6)
read = lambda: map(int, stdin.readline().rstrip().split())


def search(lo, hi):
    global tree

    mid = (lo + hi) // 2

    s = 0
    for t in tree:
        if t <= mid: break
        s += (t - mid)

    if s < m:
        return lo, mid - 1
    else:
        return mid + 1, hi


n, m = read()
tree = list(read())
tree.sort(reverse=True)

lo = 0
hi = max(tree)

while lo <= hi:
    lo, hi = search(lo, hi)

print(lo - 1)
