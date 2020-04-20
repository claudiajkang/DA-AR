from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi, v):
    global a

    mid = (lo + hi) // 2

    if a[mid] <= v:
        return mid, hi
    else:
        return lo, mid


n = int(read())
a = list(map(int, read().split()))
a.sort()

m = int(read())
b = list(map(int, read().split()))

for i in range(m):
    lo = 0
    hi = n

    while (lo + 1) < hi:
        lo, hi = bs(lo, hi, b[i])

    if a[lo] == b[i]:
        print(1)
    else:
        print(0)
