from sys import stdin

def count(n, s):
    if not n:
        return 0
    r = n // s
    i = s*s
    while i <= n:
        r += (n // i)
        i *= s
    return r

n, m = map(int, stdin.readline().split())

five = count(n, 5)
five -= count(n-m, 5)
five -= count(m, 5)

two = count(n, 2)
two -= count(n-m, 2)
two -= count(m, 2)

print(min(five, two))
