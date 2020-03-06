from sys import stdin
read = lambda: stdin.readline().rstrip()

N = int(read())
NMONEY = sorted(list(map(int, read().split())))
M = int(read())

lo = 0
hi = 10 ** 9
mid = 0
s = 0

if sum(NMONEY) <= M:
    print(max(NMONEY))

else:
    while lo <= hi:
        mid = (lo + hi) // 2

        s = 0
        for i in NMONEY:
            if i <= mid:
                s += i
            else:
                s += mid

        if s <= M:
            lo = mid + 1
        else:
            hi = mid - 1

    print(hi)
