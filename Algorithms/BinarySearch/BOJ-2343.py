from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global m, lesson, res

    mid = (lo + hi) // 2

    s = 0
    c = 0

    for l in lesson:
        if l > mid:
            return mid, hi

        s += l
        if mid < s:
            s = l
            c += 1

    if c >= m:
        return mid, hi
    else:
        return lo, mid


n, m = map(int, read().split())
lesson = list(map(int, read().split()))

lo = 0
hi = sum(lesson)
res = 0

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)
