from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def multiple(a, b):
    global c

    if 0 <= b <= 1:
        return a % c

    elif b % 2 == 0:
        r = multiple(a, b // 2)
        return (r * r) % c
    else:
        r = multiple(a, b // 2)
        return (((r * r) % c) * a) % c


a, b, c = map(int, stdin.readline().rstrip().split())

print(multiple(a, b))
