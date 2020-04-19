from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi, i):
    global nn, mm
    mid = (lo + hi) // 2

    if nn[mid] > mm[i]:
        return lo, mid

    elif nn[mid] == mm[i]:
        return mid, mid

    else:
        return mid, hi


n = int(read())
nn = list(map(int, read().split()))
nn.sort()

m = int(read())
mm = list(map(int, read().split()))

for i in range(m):
    lo = 0
    hi = n

    while (lo + 1) < hi:
        lo, hi = bs(lo, hi, i)

    print(1 if nn[lo] == mm[i] else 0)
