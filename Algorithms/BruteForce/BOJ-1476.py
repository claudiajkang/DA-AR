from sys import stdin

e, s, m = map(int, stdin.readline().rstrip().split())

te, ts, tm = 0, 0, 0
c = 0

while True:
    if e == te and s == ts and m == tm:
        break

    te += 1
    ts += 1
    tm += 1
    c += 1

    if te > 15:
        te = 1
    if ts > 28:
        ts = 1
    if tm > 19:
        tm = 1

print(c)
