from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
read = lambda: stdin.readline().rstrip()

def bs(lo, hi):
    global lan, n

    mid = (lo + hi) // 2

    c = 0
    for i in lan:
        c += (i // mid)

    if c >= n:
        return mid, hi

    else:
        return lo, mid


k, n = map(int, read().split())
lan = [int(read()) for i in range(k)]

lo = 1
hi = max(lan) + 1

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(lo)
