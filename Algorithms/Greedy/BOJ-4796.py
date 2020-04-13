from sys import stdin

read = lambda: stdin.readline().rstrip()

case = 1
while True:
    l, p, v = map(int, read().split())

    if [l, p, v] == [0, 0, 0]:
        break

    day = 0
    res = 0
    rest = False

    while day <= v:
        if rest:
            day += (p - l)
        else:
            if day + l > v:
                tr = v - day
                res += tr
                day += l
            else:
                day += l
                res += l

        rest = not rest

    print(f"Case {case}: {res}")
    case += 1
