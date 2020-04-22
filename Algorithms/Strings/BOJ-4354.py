from sys import stdin

read = lambda: stdin.readline().rstrip()

while True:
    p = read()

    if p == '.':
        break

    l = len(p)

    fail = [0] * l

    j = 0

    for i in range(1, l):
        if (j > 0) and p[i] != p[j]:
            j = fail[j - 1]

        if p[i] == p[j]:
            j += 1
            fail[i] = j

    q = fail[l - 1]
    r = l - q

    if q == 0 or (q % r != 0):
        print(1)

    else:
        print(q // r + 1)
