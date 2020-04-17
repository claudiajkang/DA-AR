from sys import stdin
read = lambda: stdin.readline().rstrip()

n, c = map(int, read().split())
p = [0] * n

for i in range(n):
    p[i] = int(read())

p.sort()
lo = 1
hi = max(p) + 1

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    count = 1
    cur = p[0]

    for i in range(1, n):
        if (cur + mid) <= p[i]:
            cur = p[i]
            count += 1

    if count >= c:
        lo = mid
    else:
        hi = mid

print(lo)

