from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def search(lo, hi):
    global lm, m

    mid = (lo + hi) // 2

    s = 0
    for l in lm:
        s += l if l < mid else mid

    if s > m:
        return lo, mid - 1
    else:
        return mid + 1, hi


n = int(read())
lm = list(map(int, read().split()))
m = int(read())
lm.sort(reverse=True)

lo = 0
hi = sum(lm)

if hi <= m:
    print(max(lm))
    exit()

while lo <= hi:
    lo, hi = search(lo, hi)

print(lo - 1)
