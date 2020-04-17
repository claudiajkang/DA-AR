from sys import stdin
read = lambda: stdin.readline().rstrip()

k, n = map(int, read().split())
lan = [0] * k

for i in range(k):
    lan[i] = int(read())

lo = 1
hi = sum(lan) + 1

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    c = 0
    for i in lan:
        c += (i // mid)

    if c >= n:
        lo = mid
    else:
        hi = mid

print(lo)