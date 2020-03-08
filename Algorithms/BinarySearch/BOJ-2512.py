from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
nm = sorted(list(map(int, read().split())), reverse=True)
m = int(read())

if sum(nm) <= m:
    print(max(nm))
    exit()

lo = 0
hi = 10 ** 9
mid = 0
s = 0

while lo <= hi:
    mid = (lo + hi) // 2
    s = 0
    for i in nm:
        if i >= mid:
            s += mid
        else:
            s += i

    if s > m:
        hi = mid - 1
    else:
        lo = mid + 1

print(hi)
