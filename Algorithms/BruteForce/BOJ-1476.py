from sys import stdin

E, S, M = map(int, stdin.readline().split())

em = 15
sm = 28
mm = 19

year = 0
es = 0
ss = 0
ms = 0

ei = 0
si = 0
mi = 0

while [E, S, M] != [ei, si, mi]:
    ei += 1
    si += 1
    mi += 1
    year += 1

    if ei > em:
        ei %= em

    if si > sm:
        si %= sm

    if mi > mm:
        mi %= mm

print(year)
