from sys import stdin

N = int(stdin.readline())
r = 1
if N > 1:
    for i in range(1, N+1):
        r *= i

print(r)
