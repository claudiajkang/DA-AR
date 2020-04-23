from sys import stdin
read = lambda: stdin.readline().rstrip()

while True:
    p = read()
    if p == '.': break

    l = len(p)
    fail = [0] * l

    j = 0

    for i in range(1, l):
        if j > 0 and p[i] != p[j]:
            j = fail[j - 1]

        if p[i] == p[j]:
            j += 1
            fail[i] = j

    p = fail[-1]
    q = l - p

    if p == 0 or (p % q != 0):
        print(1)
    else:
        print(p // q + 1)
