from sys import stdin

MAX = 1000000
PN = [False, False] + [True for i in range(2, MAX+1)]

for i in range(2, MAX+1):
    if pow(i, 2) > MAX:
        break
    if PN[i]:
        v = MAX // i
        for j in range(2, v+1):
            PN[i*j] = False

        if i % 2 == 0:
            PN[i] = False

for l in stdin:
    l = int(l)
    if l == 0:
        break

    A = -1
    for i in range(l, 2, -1):
        if PN[i] and PN[l-i]:
            A = i
            break

    if A == -1:
        print("Goldbach's conjecture is wrong.")
    else:
        print("%d = %d + %d" % (l, l-A, A))