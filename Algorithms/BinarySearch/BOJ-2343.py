from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global m, lesson, res

    mid = (lo + hi) // 2

    s = 0
    c = 0

    for l in lesson:
        if (s + l) <= mid:
            s += l
        else:
            s = l
            c += 1

    if s > 0:
        c += 1

    if c <= m:
        res = mid
        return lo, mid - 1

    else:
        return mid + 1, hi


n, m = map(int, read().split())
lesson = list(map(int, read().split()))

lo = max(lesson)
hi = sum(lesson)
res = 0

while lo <= hi:
    lo, hi = bs(lo, hi)

print(res)
