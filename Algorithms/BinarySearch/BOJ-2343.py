from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

def bs(lo, hi):
    global lesson, m

    mid = (lo + hi) // 2

    c = 0
    s = 0

    for l in lesson:
        if l > mid:
            return mid, hi

        if (s + l) <= mid:
            s += l
        else:
            s = l
            c += 1

    if s > 0:
        c += 1

    if c > m:
        return mid, hi
    else:
        return lo, mid


n, m = map(int, read().split())
lesson = list(map(int, read().split()))

lo = 0
hi = sum(lesson)

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)