from sys import stdin

read = lambda: stdin.readline().rstrip()

n, c = map(int, read().split())
pos = [int(read()) for i in range(n)]
pos.sort()

lo = 1
hi = pos[-1] + 1

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    count = 1
    before = pos[0]

    for i in range(1, n):
        if (pos[i] - before) >= mid:
            count += 1
            before = pos[i]

    if count >= c:
        lo = mid

    else:
        hi = mid

print(lo)
