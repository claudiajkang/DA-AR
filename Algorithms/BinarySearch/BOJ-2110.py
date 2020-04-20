from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

def bs(lo, hi):
    global wifi, c, n

    mid = (lo + hi) // 2

    count = 1
    before = wifi[0]

    for i in range(1, n):
        if (wifi[i] - before) >= mid:
            before = wifi[i]
            count += 1

    if count >= c:
        return mid, hi

    else:
        return lo, mid


n, c = map(int, read().split())
wifi = [int(read()) for i in range(n)]
wifi.sort()

lo = 1
hi = wifi[-1] + 1

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(lo)
