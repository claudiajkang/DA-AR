from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

class Node:
    def __init__(self, l):
        self.start = l[0]
        self.end = l[1]
        self.diff = l[2]


def bs(lo, hi):
    global box, d

    mid = (lo + hi) // 2

    c = 0

    for b in box:
        if b.start > mid: continue

        c += ((min(b.end, mid) - b.start) // b.diff) + 1

    if c >= d:
        return lo, mid
    else:
        return mid, hi


n, k, d = map(int, read().split())
box = [Node(list(map(int, read().split()))) for i in range(k)]

lo = 0
hi = n

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)
