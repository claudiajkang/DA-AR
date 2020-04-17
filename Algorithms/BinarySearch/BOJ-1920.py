from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
nint = list(map(int, read().split()))
nint.sort()
m = int(read())
mint = list(map(int, read().split()))

for i in range(m):
    lo = 0
    hi = n

    while (lo + 1) < hi:
        mid = (lo + hi) // 2

        if nint[mid] > mint[i]:
            lo = mid

        else:
            hi = mid

    if mint[lo] == mint[i]:
        print(1)
    else:
        print(0)
