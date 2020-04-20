from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))

m = int(read())
b = list(map(int, read().split()))
r = {i: 0 for i in set(a + b)}

for i in range(n):
    r[a[i]] += 1

res = []

for i in b:
    res.append(r[i])

print(' '.join(map(str, res)))
