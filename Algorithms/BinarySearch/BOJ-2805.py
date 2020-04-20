from sys import stdin

read = lambda: stdin.readline().rstrip()

def bs(lo, hi):
    global t, m

    mid = (lo + hi) // 2

    s = 0
    for h in t:
        if h > mid:
            s += (h - mid)
        else:
            break

    if s >= m:
        return mid, hi
    else:
        return lo, mid


n, m = map(int, read().split())
t = list(map(int, read().split()))
t.sort(reverse=True)

lo = 0
hi = max(t)

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(lo)
