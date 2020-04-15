from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
tree = list(read())
tree.sort(reverse=True)

lo = 0
hi = max(tree)

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    s = 0
    for h in tree:
        s += (h - mid) if h > mid else 0

    if s >= m:
        lo = mid
    else:
        hi = mid

print(lo)