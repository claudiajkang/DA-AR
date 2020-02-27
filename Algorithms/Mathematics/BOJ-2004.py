from sys import stdin

def count(n, s):
    if not n:
        return 0
    r = n // s
    i = s * s

    while i <= n:
        r += (n // i)
        i *= s

    return r

n, m = map(int, stdin.readline().split())

five = count(n, 5) - (count(m, 5) + count(n-m, 5))
two = count(n, 2) - (count(m, 2) + count(n-m, 2))

print(min(five, two))
