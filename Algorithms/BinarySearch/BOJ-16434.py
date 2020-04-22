from sys import stdin
read = lambda: stdin.readline().rstrip()


class r:
    def __init__(self, l):
        self.type = l[0]
        self.atk = l[1]
        self.hp = l[2]


n, Hatk = map(int, read().split())
room = [r(list(map(int, read().split()))) for i in range(n)]

lo = 0
hi = 10 ** 18

while (lo + 1) < hi:
    Hmax = (lo + hi) // 2

    curHp = Hmax
    curAtk = Hatk
    flag = False

    for t in room:
        if t.type == 1:
            if t.hp % curAtk:
                curHp -= ((t.hp // curAtk) * t.atk)

            else:
                curHp -= (((t.hp // curAtk) - 1) * t.atk)

            if curHp <= 0:
                flag = True
                break

        else:
            curAtk += t.atk
            curHp = min(curHp + t.hp, Hmax)

    if flag:
        lo = Hmax

    else:
        hi = Hmax

print(hi)