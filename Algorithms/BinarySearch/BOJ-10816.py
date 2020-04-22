from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))

m = int(read())
b = list(map(int, read().split()))

res = {i: 0 for i in set(a + b)}

for i in a:
    res[i] += 1

p = []
for i in b:
    p.append(res[i])

print(' '.join(map(str, p)))
