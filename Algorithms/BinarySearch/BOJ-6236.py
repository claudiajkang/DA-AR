from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = list(map(int, read().split()))
dayMoney = [0 for i in range(n)]

for i in range(n):
    dayMoney[i] = int(read())

if m == 1:
    print(sum(dayMoney))
    exit()

lo = max(dayMoney)
hi = sum(dayMoney)

while lo < hi:
    mid = (lo + hi) // 2

    s = 0
    c = 0

    for l in dayMoney:
        if (s + l) <= mid:
            s += l
        else:
            s = l
            c += 1

    if s > 0:
        c += 1

    if c > m:
        lo = mid + 1
    else:
        hi = mid

print(lo)
