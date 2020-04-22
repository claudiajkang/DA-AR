from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def histogram(s, e):
    global hh

    if s == e: return 0
    if s + 1 == e: return hh[s]

    mid = (s + e) // 2
    result = max(histogram(s, mid), histogram(mid, e))

    w = 1
    h = hh[mid]
    l = mid
    r = mid

    while (r - l + 1) < (e - s):
        p = min(h, hh[l - 1]) if l > s else -1
        q = min(h, hh[r + 1]) if r < e - 1 else -1

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
hh = [int(read()) for i in range(n)]

print(histogram(0, n))
