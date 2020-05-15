from sys import stdin

read = lambda: stdin.readline().rstrip()

n, l = map(int, read().split())
b = list(map(int, read().split()))
b.sort()

res = 1
before = b[0] + l - 1

for t in b[1:]:
    if t <= before:
        continue
    else:
        res += 1
        before = t + l - 1

print(res)