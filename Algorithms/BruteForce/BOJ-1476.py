from sys import stdin

e, s, m = map(int, stdin.readline().rstrip().split())

if e == s and s == m:
    print(s)
    exit()

else:
    te = ts = tm = 0
    y = 0

    while not (te == e and ts == s and tm == m):
        te += 1
        ts += 1
        tm += 1
        y += 1

        if te > 15: te = 1
        if ts > 28 : ts = 1
        if tm > 19 : tm = 1

    print(y)

