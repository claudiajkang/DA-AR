from sys import stdin

def count(n, s):
    c = 0

    while n > 0:
        n //= s
        c += n

    return c

n, m = map(int, stdin.readline().split())

five = count(n, 5) - (count(m, 5) + count(n-m, 5))
two = count(n, 2) - (count(m, 2) + count(n-m, 2))

print(min(five, two))
