from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()

def bs(lo, hi, v):
    global a

    mid = (lo + hi) // 2

    if a[mid] > v:
        return lo, mid
    else:
        return mid, hi


n = int(read())
a = list(map(int, read().split()))
a.sort()

m = int(read())
b = list(map(int, read().split()))

res = [0] * m

for i in range(m):
    lo = 0
    hi = n - 1

    if a[n-1] == b[i]:
        res[i] = 1
        continue

    while (lo + 1) < hi:
        lo, hi = bs(lo, hi, b[i])

    res[i] = 1 if a[lo] == b[i] else 0

print(' '.join(map(str, res)))