from sys import stdin
read = lambda: stdin.readline().rstrip()

case = 1
while True:
    l, p, v = map(int, read().split())

    if [l, p, v] == [0, 0, 0]: break

    day = 0
    rest = False
    res = 0

    while day <= v:
        if rest:
            day += (p - l)

        else:
            if (day + l) > v:
                res += (v - day)
            else:
                res += l
            day += l

        rest = not rest

    print(f"Case {case}: {res}")
    case += 1