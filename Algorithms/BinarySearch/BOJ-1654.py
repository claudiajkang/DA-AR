from sys import stdin

read = lambda: stdin.readline().rstrip()

k, n = map(int, read().split())
lan = [0 for i in range(k)]

for i in range(k):
    lan[i] = int(read())

lo = 1
hi = max(lan) + 1

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    c = 0
    for l in lan:
        c += (l // mid)

    if c < n:
        hi = mid
    else:
        lo = mid

print(lo)
