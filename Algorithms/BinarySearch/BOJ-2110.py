from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def bs(lo, hi):
    global pos, c, n, res

    mid = (lo + hi) // 2

    count = 1
    s = pos[0]

    for i in range(1, n):
        if (s + mid) <= pos[i]:
            count += 1
            s = pos[i]

    if count >= c:
        res = mid
        return mid + 1, hi
    else:
        return lo, mid - 1


n, c = map(int, read().split())
pos = [int(read()) for i in range(n)]
pos.sort()

lo = 1
hi = pos[-1] - pos[0]
res = 0

while lo <= hi:
    lo, hi = bs(lo, hi)

print(res)
