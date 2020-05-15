from sys import stdin

e, s, m = map(int, stdin.readline().rstrip().split())
te, ts, tm = 0, 0, 0
y = 0

while not (e == te and s == ts and m == tm):
    te += 1
    ts += 1
    tm += 1
    y += 1

    if te == 16:
        te = 1

    if ts == 29:
        ts = 1

    if tm == 20:
        tm = 1

print(y)