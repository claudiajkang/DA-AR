from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())
b = list(read().split())
ch = []

if n == 100:
    print(0)
    exit()

for i in range(0, 1000001):
    f = 0
    for tb in b:
        if tb in str(i):
            f = 1
            break
    if not f:
        ch.append(i)

res = abs(n - 100)

for i in ch:
    if abs(i-n) + len(str(i)) < res:
        res = abs(i-n) + len(str(i))
print(res)
