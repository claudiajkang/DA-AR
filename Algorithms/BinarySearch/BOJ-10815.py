from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
a.sort()

m = int(read())
b = list(map(int, read().split()))

res = []
for i in range(m):
    if b[i] == a[n - 1]:
        res.append(1)
        continue
    lo = 0
    hi = n - 1

    while (lo + 1) < hi:
        mid = (lo + hi) // 2

        if a[mid] > b[i]:
            hi = mid
        else:
            lo = mid

    res.append(1 if a[lo] == b[i] else 0)

print(' '.join(map(str, res)))