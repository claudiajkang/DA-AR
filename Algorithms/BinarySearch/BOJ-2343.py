from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def possible(maxTime):
    global m, n, time
    s = 0
    limit = m

    for i in range(n):
        if time[i] > maxTime:
            return False
        s += time[i]

        if maxTime < s:
            if limit == 1:
                return False

            limit -= 1
            s = time[i]

    return True


n, m = map(int, read().split())
time = list(map(int, read().split()))

lo = 0
hi = sum(time)

while (lo + 1) < hi:
    mid = (lo + hi) // 2

    if possible(mid):
        hi = mid
    else:
        lo = mid

print(hi)
