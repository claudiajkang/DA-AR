from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


class Node:
    def __init__(self, l):
        self.start = l[0]
        self.end = l[1]
        self.diff = l[2]


def bs(lo, hi):
    global d, dotori

    mid = (lo + hi) // 2
    count = 0

    for t in dotori:
        if t.start > mid:
            continue
        else:
            count += ((min(mid, t.end) - t.start) // t.diff + 1)

    if count < d:
        return mid, hi

    else:
        return lo, mid


n, k, d = map(int, read().split())
dotori = [Node(list(map(int, read().split()))) for i in range(k)]

lo = 0
hi = n

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)