from sys import stdin

read = lambda: stdin.readline().rstrip()


class Node:
    def __init__(self):
        self.t = 0
        self.a = 0
        self.h = 0


N, Atk = map(int, read().split())
room = [Node() for i in range(N + 1)]

for i in range(1, N + 1):
    t, a, h = map(int, read().split())
    room[i].t = t
    room[i].a = a
    room[i].h = h

lo = 1
hi = (10 ** 12) * (10 ** 6) + 1

while lo <= hi:
    Hmaxhp = (lo + hi) // 2

    Hcurhp = Hmaxhp
    Hatk = Atk

    for i in range(1, N + 1):
        if room[i].t == 1:
            if room[i].h % Hatk == 0:
                Hcurhp -= (room[i].a * ((room[i].h // Hatk) - 1))

            else:
                Hcurhp -= (room[i].a * (room[i].h // Hatk))

        elif room[i].t == 2:
            Hatk += room[i].a
            Hcurhp += room[i].h
            if Hcurhp > Hmaxhp: Hcurhp = Hmaxhp

        if Hcurhp <= 0:
            break

    if Hcurhp > 0:
        hi = Hmaxhp - 1
    else:
        lo = Hmaxhp + 1

print(lo)
