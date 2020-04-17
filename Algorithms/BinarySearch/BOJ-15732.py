from sys import stdin

read = lambda: stdin.readline().rstrip()


class rules:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.diff = 0


n, k, d = map(int, read().split())
r = [rules() for i in range(k)]

for i in range(k):
    temp = list(map(int, read().split()))
    r[i].start = temp[0]
    r[i].end = temp[1]
    r[i].diff = temp[2]

lo = 1
hi = n

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    s = 0
    for i in range(k):
        if r[i].start <= mid:
            s += ((min(r[i].end, mid) - r[i].start) // r[i].diff + 1)

    if s >= d:
        hi = mid

    else:
        lo = mid

print(hi)
