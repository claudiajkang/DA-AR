from sys import stdin

while True:
    s = stdin.readline().rstrip()

    if s == '.': break

    l = len(s)
    fail = [0] * l

    j = 0
    for i in range(1, l):
        if j > 0 and s[i] != s[j]:
            j = fail[j - 1]

        if s[i] == s[j]:
            j += 1
            fail[i] = j

    p = fail[-1]
    q = l - p

    if q == 0 or (p % q != 0):
        print(1)
    else:
        print(p // q + 1)