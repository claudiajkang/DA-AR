from sys import stdin

A, B = map(int, stdin.readline().split())
m = int(stdin.readline())
num = list(map(int, stdin.readline().strip().split()))
v = 0
res = []

for i in range(m):
    v += num[m-i-1] * pow(A, i)

while v:
    v, r = divmod(v, B)
    res.insert(0, str(r))

print(' '.join(res))
