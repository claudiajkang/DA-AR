from sys import stdin

A, B = map(int, stdin.readline().split())
M = int(stdin.readline())
V = list(map(int, stdin.readline().split()))
digit = 0

for i in range(M):
    digit += (V[M-i-1] * pow(A, i))

res = []
while digit:
    digit, r = divmod(digit, B)
    res.append(str(r))

print(' '.join(reversed(res)))
