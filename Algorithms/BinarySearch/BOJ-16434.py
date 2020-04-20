from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()

class Node:
    def __init__(self, l):
        self.type = l[0]
        self.atk = l[1]
        self.hp = l[2]


def bs(lo, hi):
    global room, Hatk

    maxhp = (lo + hi) // 2
    curhp = maxhp
    curatk = Hatk

    for r in room:
        if r.type == 1:
            if r.hp % curatk:
                curhp -= (r.hp // curatk) * r.atk

            else:
                curhp -= ((r.hp // curatk) - 1) * r.atk

            if curhp <= 0:
                return maxhp, hi

        else:
            curatk += r.atk
            curhp = min(curhp + r.hp, maxhp)

    return lo, maxhp


n, Hatk = map(int, read().split())
room = [Node(list(map(int, read().split()))) for i in range(n)]

lo = 0
hi = 10 ** 18

while (lo + 1) < hi:
    lo, hi = bs(lo, hi)

print(hi)