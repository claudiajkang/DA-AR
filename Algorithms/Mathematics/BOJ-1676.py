from sys import stdin
read = lambda : stdin.readline().rstrip()

def count(n, s):
    c = 0

    while n > 0:
        n //= s
        c += n

    return c

N = int(read())

print(min(count(N,5), count(N,2)))
