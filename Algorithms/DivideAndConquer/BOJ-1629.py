from sys import stdin


def cal(a, b, c):
    if 0 <= b <= 1:
        return a % c
    if b % 2 == 0:
        r = cal(a, b // 2, c)
        return (r * r) % c

    else:
        r = cal(a, b // 2, c)
        return (((r * r) % c) * a) % c


A, B, C = map(int, stdin.readline().rstrip().split())
print(cal(A, B, C))
