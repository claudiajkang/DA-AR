from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

l, m = read()
lesson = list(read())

lo = max(lesson)
hi = sum(lesson)

while lo < hi:
    mid = (lo + hi) // 2

    s = 0
    c = 0

    for l in lesson:
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
