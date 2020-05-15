from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def multiple(a, b):
    global c

    if b == 1:
        return a % c

    else:
        t = multiple(a, b // 2)
        if b % 2:
            return (((t * t) % c) * a) % c
        else:
            return (t * t) % c


a, b, c = map(int, stdin.readline().rstrip().split())
print(multiple(a, b) % c)