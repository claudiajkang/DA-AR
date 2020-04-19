from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global n, c, pos

    mid = (lo + hi) // 2

    count = 1
    before = pos[0]

    for i in range(1, n):
        if (pos[i] - before) >= mid:
            before = pos[i]
            count += 1

    if count >= c:
        return mid, hi

    else:
        return lo, mid


n, c = map(int, read().split())
pos = [int(read()) for i in range(n)]
pos.sort()

lo = 1
hi = pos[-1] + 1

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(lo)
