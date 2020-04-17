from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
money = [0] * n

for i in range(n):
    money[i] = int(read())

if m == 1:
    print(sum(money))

else:
    lo = max(money)
    hi = sum(money)

    while lo < hi:
        mid = (lo + hi) // 2

        s = 0
        c = 0

        for mm in money:
            if (s + mm) <= mid:
                s += mm
            else:
                s = mm
                c += 1

        if s > 0:
            c += 1

        if c > m:
            lo = mid + 1

        else:
            hi = mid

    print(lo)
