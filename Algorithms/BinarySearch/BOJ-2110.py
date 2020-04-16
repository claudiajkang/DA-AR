from sys import stdin

read = lambda: stdin.readline().rstrip()

n, c = map(int, read().split())
h = [0] * n

for i in range(n):
    h[i] = int(read())

h.sort()

lo = 1
hi = h[-1] + 1

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    cur = h[0]
    count = 1

    for i in range(1, n):
        if (cur + mid) <= h[i]:
            cur = h[i]
            count += 1

    if count >= c:
        lo = mid
    else:
        hi = mid

print(lo)
