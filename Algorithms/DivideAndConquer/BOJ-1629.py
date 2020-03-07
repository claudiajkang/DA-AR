from sys import stdin


def cal(a, b, c):
    if 0 <= b <= 1:
        return a % c
    r = cal(a, b // 2, c)
    if b % 2:
        return (((r * r) % c) * a) % c
    else:
        return (r * r) % c


A, B, C = map(int, stdin.readline().rstrip().split())

print(cal(A, B, C))
