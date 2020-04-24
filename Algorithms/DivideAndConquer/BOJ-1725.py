from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

def histogram(lo, hi):
    global height

    if lo == hi:
        return 0

    if lo + 1 == hi:
        return height[lo]

    mid = (lo + hi) // 2
    result = max(histogram(lo, mid), histogram(mid, hi))

    w = 1
    h = height[mid]
    l = mid
    r = mid

    while (r - l + 1) < (hi - lo):
        p = min(h, height[l - 1]) if l > lo else -1
        q = min(h, height[r + 1]) if r < hi - 1 else -1

        if p >= q:
            h = p
            l -= 1

        else:
            h = q
            r += 1

        w += 1
        result = max(result, w * h)

    return result


n = int(read())
height = [int(read()) for i in range(n)]

print(histogram(0, n))