from sys import stdin
  
def count(n, s):
    c = 0

    while n > 0:
        n = n // s
        c += n

    return c

N, M = map(int, stdin.readline().split())

f = count(N, 5) - (count(M, 5) + count(N-M, 5))
t = count(N, 2) - (count(M, 2) + count(N-M, 2))

print(min(f,t))
