from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


class Node:
    def __init__(self, l):
        self.t = l[0]
        self.a = l[1]
        self.h = l[2]


def search(lo, hi):
    global Hatk, room, n

    mid = (lo + hi) // 2

    atk = Hatk
    curhp = mid

    for r in room:
        if r.t == 1:
            if r.h % atk == 0:
                curhp -= (r.a * ((r.h // atk) - 1))

            else:
                curhp -= (r.a * (r.h // atk))

            if curhp <= 0:
                return mid, hi

        elif r.t == 2:
            atk += r.a
            curhp = min(curhp + r.h, mid)

    return lo, mid


n, Hatk = map(int, read().split())
room = [Node(list(map(int, read().split()))) for i in range(n)]

lo = 0
hi = (10 ** 12) * (10 ** 6)

while (lo + 1) < hi:
    lo, hi = search(lo, hi)

print(hi)
