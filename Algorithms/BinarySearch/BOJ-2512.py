from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
l = list(map(int, read().split()))
l.sort()
m = int(read())

if sum(l) <= m:
    print(max(l))
    exit()

lo = 0
hi = 10 ** 9
mid = 0
s = 0

while lo <= hi:
    mid = (lo + hi) // 2

    s = 0
    for i in l:
        if i >= mid:
            s += mid
        else:
            s += i

    if s > m:
        hi = mid - 1

    else:
        lo = mid + 1

print(hi)
