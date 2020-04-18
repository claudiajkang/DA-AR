from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global lan, n

    mid = (lo + hi) // 2

    c = 0
    for l in lan:
        c += (l // mid)

    if c < n:
        return lo, mid - 1
    else:
        return mid + 1, hi


k, n = map(int, read().split())
lan = [int(read()) for i in range(k)]

lo = 1
hi = max(lan) + 1

while lo <= hi:
    lo, hi = bs(lo, hi)

print(hi)
