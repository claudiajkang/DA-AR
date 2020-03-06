from sys import stdin
read = lambda: stdin.readline().rstrip()

K, N = map(int, read().split())
L = [0] * K

for i in range(K):
    L[i] = int(read())

L = sorted(L)
lo = 0
hi = max(L)
mid = 0
s = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if mid == 0:
        break

    s = 0
    for i in L:
        s += (i // mid)

    if s >= N:
        lo = mid + 1

    else:
        hi = mid - 1

print(hi)
